from typing import Any

import httpx
from httpx_auth import OAuth2ClientCredentials, OAuth2ResourceOwnerPasswordCredentials

from .base import ApiModelBase, ClientBase, ModelClass
from .config import AdminConfig, StoreConfig
from .endpoints.admin import AdminEndpoints
from .endpoints.store import StoreEndpoints
from .exceptions import SWAPIConfigException


class AdminClient(ClientBase, AdminEndpoints):
    def __init__(self, config: AdminConfig, raw: bool = False):
        super().__init__(config, raw=raw)
        self.config = config
        self.api_url = f"{config.url}/api"
        self._client: httpx.AsyncClient | None = None
        self.init_endpoints(self)

    def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                event_hooks={"request": [self.log_request], "response": [self.log_response]}
            )

            auth_url = f"{self.api_url}/oauth/token"

            if self.config.grant_type == "client_credentials":
                if self.config.client_id is not None and self.config.client_secret is not None:
                    self._client.auth = OAuth2ClientCredentials(
                        token_url=auth_url, client_id=self.config.client_id, client_secret=self.config.client_secret
                    )
                else:
                    raise SWAPIConfigException("Missing Client Credentials.")
            elif self.config.grant_type == "password":
                if self.config.username is not None and self.config.password is not None:
                    self._client.auth = OAuth2ResourceOwnerPasswordCredentials(
                        token_url=auth_url, username=self.config.username, password=self.config.password
                    )
                else:
                    raise SWAPIConfigException("Missing Client Credentials.")
            else:
                raise SWAPIConfigException("Invalid grant_type for AdminClient.")

        return self._client

    async def bulk_upsert(
        self, name: str, objs: list[ModelClass] | list[dict[str, Any]], **request_kwargs: dict[str, Any]
    ) -> dict[str, Any] | None:
        obj_list: list[dict] = []

        for obj in objs:
            if isinstance(obj, ApiModelBase):
                obj_list.append(obj.model_dump(by_alias=True, mode="json", exclude_unset=True))
            else:
                obj_list.append(obj)

        data = {f"write-{name}": {"entity": name, "action": "upsert", "payload": obj_list}}

        response = await self.post("/_action/sync", json=data, timeout=600, **request_kwargs)
        result: dict[str, Any] = response.json()

        return result

    async def bulk_delete(
        self, name: str, objs: list[ModelClass] | list[dict[str, Any]], **request_kwargs: dict[str, Any]
    ) -> dict[str, Any]:
        obj_list: list[dict] = []

        for obj in objs:
            if isinstance(obj, ApiModelBase):
                obj_list.append(obj.model_dump(by_alias=True, mode="json", exclude_unset=True))
            else:
                obj_list.append(obj)

        data = {f"delete-{name}": {"entity": name, "action": "delete", "payload": obj_list}}

        response = await self.post("/_action/sync", json=data, timeout=600, **request_kwargs)
        result: dict[str, Any] = response.json()

        return result


class StoreClient(ClientBase, StoreEndpoints):
    def __init__(self, config: StoreConfig, raw: bool = False):
        super().__init__(config, raw=raw)
        self.config = config
        self.api_url = f"{config.url}/store-api"
        self._client: httpx.AsyncClient | None = None
        self.init_endpoints(self)

    def _get_client(self) -> httpx.AsyncClient:
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

            self._client.headers = httpx.Headers(headers)

        return self._client
