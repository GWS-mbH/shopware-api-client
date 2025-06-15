import json
from typing import Any, Callable, Generator, Literal, cast

import httpx
from httpx_auth import OAuth2, OAuth2ClientCredentials, OAuth2ResourceOwnerPasswordCredentials, TokenMemoryCache
from redis.client import Redis

from .base import ApiModelBase, ClientBase, ModelClass
from .config import AdminConfig, StoreConfig
from .endpoints.admin import AdminEndpoints
from .endpoints.store import StoreEndpoints
from .exceptions import SWAPIConfigException, SWAPIError, SWAPIErrorList


class AdminClient(ClientBase, AdminEndpoints):
    def __init__(self, config: AdminConfig, raw: bool = False) -> None:
        super().__init__(config, raw=raw)
        self.config = config
        self.api_url = f"{config.url}/api"
        self._client: httpx.AsyncClient | None = None
        self.init_endpoints(self)

    def _get_http_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                event_hooks={"request": [self.log_request], "response": [self.log_response]},
                **self.httpx_init_kwargs,
            )

            # increase default(10s) timeouts
            self._client.timeout = httpx.Timeout(15, read=45, write=45)

            auth_url = f"{self.api_url}/oauth/token"

            if self.config.grant_type == "client_credentials":
                if self.config.client_id is not None and self.config.client_secret is not None:
                    # determine if we want to use redis cache backend for oauth caching
                    if (redis_client := self.config.extra.pop("redis_cache_client", None)) is not None:  # type: ignore
                        TokenMemoryCacheRedis.redis_client = redis_client
                        auth_class = OAuth2ClientCredentialsRedisCached  # type: ignore
                    else:
                        auth_class = OAuth2ClientCredentials  # type: ignore

                    # init auth
                    self._client.auth = auth_class(
                        client=httpx.Client(**self.httpx_init_kwargs),
                        token_url=auth_url,
                        client_id=self.config.client_id,
                        client_secret=self.config.client_secret,
                        **self.config.extra,
                    )
                else:
                    raise SWAPIConfigException("Missing Client Credentials.")
            elif self.config.grant_type == "password":
                if self.config.username is not None and self.config.password is not None:
                    # determine if we want to use redis cache backend for oauth caching
                    if (redis_client := self.config.extra.pop("redis_cache_client", None)) is not None:  # type: ignore
                        TokenMemoryCacheRedis.redis_client = redis_client
                        auth_class = OAuth2ResourceOwnerPasswordCredentialsRedisCached  # type: ignore
                    else:
                        auth_class = OAuth2ResourceOwnerPasswordCredentials  # type: ignore

                    # init auth
                    self._client.auth = auth_class(
                        client=httpx.Client(**self.httpx_init_kwargs),
                        token_url=auth_url,
                        username=self.config.username,
                        password=self.config.password,
                        **self.config.extra,
                    )
                else:
                    raise SWAPIConfigException("Missing Client Credentials.")
            else:
                raise SWAPIConfigException("Invalid grant_type for AdminClient.")

        return self._client

    def _merge_results(self, dict1: dict[str, Any], dict2: dict[str, Any]) -> dict[str, Any]:
        for key in dict2:
            if key in dict1:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    self._merge_results(dict1[key], dict2[key])
                elif isinstance(dict1[key], list) and isinstance(dict2[key], list):
                    dict1[key].extend(dict2[key])
            else:
                dict1[key] = dict2[key]
        return dict1

    async def _retry_bulk_parts(
        self,
        action: Literal["upsert", "delete"],
        name: str,
        objs: list[ModelClass] | list[dict[str, Any]],
        exception: SWAPIError | SWAPIErrorList,
        **request_kwargs: Any,
    ) -> dict[str, Any]:
        result_dict: dict[str, Any] = {}

        if isinstance(exception, SWAPIErrorList):
            errors = exception.errors
        else:
            errors = [exception]

        if len(objs) == len(errors):
            error_list = []

            for idx, obj in enumerate(objs, start=0):
                if isinstance(obj, ApiModelBase):
                    obj = json.loads(obj.model_dump_json())

                error_list.append({"code": errors[idx].code, "detail": errors[idx].detail, "object": obj})
            return {"errors": error_list}

        split = int(len(objs) / 2)

        for part in [objs[:split], objs[split:]]:
            if action == "upsert":
                result = await self.bulk_upsert(name=name, objs=part, fail_silently=True, **request_kwargs)
            else:
                result = await self.bulk_delete(name=name, objs=part, fail_silently=True, **request_kwargs)

            if result is not None:
                self._merge_results(result_dict, result)

        return result_dict

    async def bulk_upsert(
        self,
        name: str,
        objs: list[ModelClass] | list[dict[str, Any]],
        fail_silently: bool = False,
        **request_kwargs: Any,
    ) -> dict[str, Any]:
        obj_list: list[dict] = []

        for obj in objs:
            if isinstance(obj, ApiModelBase):
                obj_list.append(obj.model_dump(by_alias=True, mode="json", exclude_unset=True))
            else:
                obj_list.append(obj)

        data = {f"write-{name}": {"entity": name, "action": "upsert", "payload": obj_list}}

        request_kwargs.setdefault("timeout", 600)

        try:
            response = await self.post("/_action/sync", json=data, **request_kwargs)
        except (SWAPIErrorList, SWAPIError) as e:
            if not fail_silently:
                raise

            result = await self._retry_bulk_parts(action="upsert", name=name, objs=objs, exception=e, **request_kwargs)
        else:
            result = response.json()

        return result

    async def bulk_delete(
        self,
        name: str,
        objs: list[ModelClass] | list[dict[str, Any]],
        fail_silently: bool = False,
        **request_kwargs: Any,
    ) -> dict[str, Any]:
        obj_list: list[dict] = []

        for obj in objs:
            if isinstance(obj, ApiModelBase):
                obj_list.append(obj.model_dump(by_alias=True, mode="json", exclude_unset=True))
            else:
                obj_list.append(obj)

        data = {f"delete-{name}": {"entity": name, "action": "delete", "payload": obj_list}}

        request_kwargs.setdefault("timeout", 600)
        # remove indexing-behavior queing behavior because it's not supported in bulk delete.
        request_kwargs.setdefault("headers", {}).pop("indexing-behavior", None)

        try:
            response = await self.post("/_action/sync", json=data, **request_kwargs)
        except (SWAPIErrorList, SWAPIError) as e:
            if not fail_silently:
                raise

            result = await self._retry_bulk_parts(action="delete", name=name, objs=objs, exception=e, **request_kwargs)
        else:
            if hasattr(response, "json_cached"):
                result = response.json_cached
            else:
                result = response.json()

        return result


class StoreClient(ClientBase, StoreEndpoints):
    def __init__(self, config: StoreConfig, raw: bool = False):
        super().__init__(config, raw=raw)
        self.config = config
        self.api_url = f"{config.url}/store-api"
        self._client: httpx.AsyncClient | None = None
        self.init_endpoints(self)

    def _get_http_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                event_hooks={"request": [self.log_request], "response": [self.log_response]},
                **self.httpx_init_kwargs,
            )

            headers = {
                "sw-access-key": self.config.access_key,
                "Accept": "application/json",
                "Content-Type": "application/json",
            }

            if self.config.context_token is not None:
                headers["sw-context-token"] = self.config.context_token

            # increase default(10s) timeouts
            self._client.timeout = httpx.Timeout(15, read=45, write=45)

            self._client.headers = httpx.Headers(headers)

        return self._client


#
# httpx_auth.TokenMemoryCache that uses redis as additional cache backend
#


class TokenMemoryCacheRedis(TokenMemoryCache):
    # will be injected by AdminClient
    redis_client: Redis | None = None

    def get_token(
        self,
        key: str,
        *,
        early_expiry: float = 30.0,
        on_missing_token: Callable | None = None,
        on_expired_token: Callable | None = None,
        **on_missing_token_kwargs: dict,
    ) -> str:
        redis_client = self.__class__.redis_client  # type: ignore
        if isinstance(redis_client, Redis) and key not in self.tokens:
            # restore token from redis cache
            redis_cached = cast(str, redis_client.get(f"httpx_oauth_token_{key}"))
            if redis_cached:
                self.tokens[key] = json.loads(redis_cached)

        return cast(
            str,
            super().get_token(
                key,
                early_expiry=early_expiry,
                on_missing_token=on_missing_token,
                on_expired_token=on_expired_token,
                **on_missing_token_kwargs,
            ),
        )

    def _add_token(self, key: str, token: str, expiry: float, refresh_token: str | None = None) -> None:
        """
        Set the bearer token and save it
        :param key: key identifier of the token
        :param token: value
        :param expiry: UTC timestamp of expiry
        :param refresh_token: refresh token value
        """
        redis_client = self.__class__.redis_client  # type: ignore
        if isinstance(redis_client, Redis):
            # also store token in redis cache
            redis_client.set(
                f"httpx_oauth_token_{key}", json.dumps((token, expiry, refresh_token)), px=int(expiry * 1000)
            )

        super()._add_token(key, token, expiry, refresh_token)

    def clear(self) -> None:
        redis_client = self.__class__.redis_client  # type: ignore
        if isinstance(redis_client, Redis):
            # delete token cache keys
            for key in redis_client.scan_iter("httpx_oauth_token_*"):
                redis_client.delete(key)
        super().clear()


class OAuth2RedisCached(OAuth2):
    token_cache = TokenMemoryCacheRedis()


class OAuth2ClientCredentialsRedisCached(OAuth2ClientCredentials):
    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        """
        Overload auth_flow to inject OAuth2RedisCached.
        """
        token = OAuth2RedisCached.token_cache.get_token(
            self.state,
            early_expiry=self.early_expiry,
            on_missing_token=self.request_new_token,
        )
        request.headers[self.header_name] = self.header_value.format(token=token)
        yield request


class OAuth2ResourceOwnerPasswordCredentialsRedisCached(OAuth2ResourceOwnerPasswordCredentials):
    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        """
        Overload auth_flow to inject OAuth2RedisCached.
        """
        token = OAuth2RedisCached.token_cache.get_token(
            self.state,
            early_expiry=self.early_expiry,
            on_missing_token=self.request_new_token,
            on_expired_token=self.refresh_token,
        )
        request.headers[self.header_name] = self.header_value.format(token=token)
        yield request
