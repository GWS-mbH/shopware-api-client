import json
from typing import Any, Literal

import httpx
from httpx_auth import OAuth2ClientCredentials, OAuth2ResourceOwnerPasswordCredentials

from .base import ApiModelBase, ClientBase, ModelClass
from .config import AdminConfig, StoreConfig
from .endpoints.admin import AdminEndpoints
from .endpoints.store import StoreEndpoints
from .exceptions import SWAPIConfigException, SWAPIError, SWAPIErrorList


class AdminClient(ClientBase, AdminEndpoints):
    def __init__(self, config: AdminConfig, raw: bool = False):
        super().__init__(config, raw=raw)
        self.config = config
        self.api_url = f"{config.url}/api"
        self._client: httpx.AsyncClient | None = None
        self.init_endpoints(self)

    def _get_http_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                event_hooks={"request": [self.log_request], "response": [self.log_response]}
            )

            # increase default(10s) timeouts
            self._client.timeout = httpx.Timeout(15, read=45, write=45)

            auth_url = f"{self.api_url}/oauth/token"

            if self.config.grant_type == "client_credentials":
                if self.config.client_id is not None and self.config.client_secret is not None:
                    self._client.auth = OAuth2ClientCredentials(
                        token_url=auth_url,
                        client_id=self.config.client_id,
                        client_secret=self.config.client_secret,
                        **self.config.extra,
                    )
                else:
                    raise SWAPIConfigException("Missing Client Credentials.")
            elif self.config.grant_type == "password":
                if self.config.username is not None and self.config.password is not None:
                    self._client.auth = OAuth2ResourceOwnerPasswordCredentials(
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
