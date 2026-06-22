from typing import Any, cast

from httpx2 import AsyncClient, AsyncHTTPTransport, Headers, Timeout

from shopware_api_client.auth import ShopwareAdminAPIAuth, ShopwareAdminPasswordAPIAuth

from .base import ApiModelBase, ClientBase, ModelClass
from .config import AdminConfig, StoreConfig
from .endpoints.admin import AdminEndpoints
from .endpoints.store import StoreEndpoints
from .exceptions import SWAPIConfigException


class AdminClient(ClientBase, AdminEndpoints):
    def __init__(self, config: AdminConfig):
        super().__init__(config=config)
        self.config = config
        self.api_url = f"{config.url}/api"
        self._client: AsyncClient | None = None

    def _get_http_client(self) -> AsyncClient:
        if self._client is None:
            self._client = AsyncClient(
                event_hooks={"request": [self.log_request], "response": [self.log_response]},
                transport=AsyncHTTPTransport(retries=1),
            )

            # increase default(10s) timeouts
            self._client.timeout = Timeout(15, read=45, write=45)

            if self.config.grant_type == "client_credentials":
                if self.config.client_id is not None and self.config.client_secret is not None:
                    self._client.auth = ShopwareAdminAPIAuth(self.config)
                else:
                    raise SWAPIConfigException("Missing Client Credentials.")

            elif self.config.grant_type == "password":
                if self.config.username is not None and self.config.password is not None:
                    self._client.auth = ShopwareAdminPasswordAPIAuth(self.config)
                else:
                    raise SWAPIConfigException("Missing Client Credentials.")
            else:
                raise SWAPIConfigException("Invalid grant_type for AdminClient.")

        return self._client

    async def bulk_upsert(
        self,
        name: str,
        objs: list[ModelClass] | list[dict[str, Any]],
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
        response = await self.post("/_action/sync", json=data, orig_objs=objs, **request_kwargs)

        return cast(dict[str, Any], response.json())

    async def bulk_delete(
        self,
        name: str,
        objs: list[ModelClass] | list[dict[str, Any]],
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

        response = await self.post("/_action/sync", json=data, orig_objs=objs, **request_kwargs)

        return cast(dict, getattr(response, "json_cached", response.json()))


class StoreClient(ClientBase, StoreEndpoints):
    def __init__(self, config: StoreConfig):
        super().__init__(config)
        self.config = config
        self.api_url = f"{config.url}/store-api"
        self._client: AsyncClient | None = None
        self.init_endpoints(self)

    def _get_http_client(self) -> AsyncClient:
        if self._client is None:
            self._client = AsyncClient(
                event_hooks={"request": [self.log_request], "response": [self.log_response]},
                transport=AsyncHTTPTransport(retries=1),
            )

            headers = {
                "sw-access-key": self.config.access_key,
                "Accept": "application/json",
                "Content-Type": "application/json",
            }

            if self.config.context_token is not None:
                headers["sw-context-token"] = self.config.context_token

            # increase default(10s) timeouts
            self._client.timeout = Timeout(15, read=45, write=45)
            self._client.headers = Headers(headers)

        return self._client
