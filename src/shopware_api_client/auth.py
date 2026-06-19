from functools import cached_property
from typing import AsyncGenerator

from httpx2 import AsyncClient, AsyncHTTPTransport, Auth, Request, Response

from shopware_api_client.config import AdminConfig


class ShopwareAdminAPIAuth(Auth):

    def __init__(self, config: AdminConfig):
        self.config = config
        self.auth_url = f"{config.url}/api/oauth/token"

    async def _get_access_token_from_shopware(self) -> tuple[str, int]:
        assert isinstance(self.config, AdminConfig), "Config must be of type AdminConfig"

        payload = {
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "grant_type": "client_credentials",
            **self.config.extra,
        }

        transport = AsyncHTTPTransport(retries=1)
        async with AsyncClient(transport=transport) as client:
            response = await client.post(self.auth_url, data=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("access_token"), data.get("expires_in")

    @cached_property
    def _cache_key(self):
        return f"shopware_api_client:access_token:client_credentials:{self.auth_url}"

    async def _get_access_token(self) -> str:
        # do we have a cached token and is it still valid?
        token = await self.config.cache.get(self._cache_key)

        if not token:
            # If not, get a new one from Shopware.
            token, expires_in = await self._get_access_token_from_shopware()
            await self.config.cache.set(self._cache_key, token, expires_in - 10)  # cache a bit less than actual expiry

        return token

    async def async_auth_flow(self, request: Request) -> AsyncGenerator[Request, Response]:

        access_token = await  self._get_access_token()
        request.headers["Authorization"] = f"Bearer {access_token}"

        async for req in super().async_auth_flow(request):
            yield req


class ShopwareAdminPasswordAPIAuth(ShopwareAdminAPIAuth):

    @cached_property
    def _cache_key(self):
        return f"shopware_api_client:access_token:password:{self.auth_url}"

    async def _get_access_token_from_shopware(self) -> tuple[str, int]:
        assert isinstance(self.config, AdminConfig), "Config must be of type AdminConfig"

        payload = {
            "client_id": "administration",
            "scopes": "write",
            "grant_type": "password",
            "username": self.config.username,
            "password": self.config.password,
            **self.config.extra,
        }

        transport = AsyncHTTPTransport(retries=1)
        async with AsyncClient(transport=transport) as client:
            response = await client.post(self.auth_url, data=payload)
            response.raise_for_status()
            data =  response.json()
            return data.get("access_token"), data.get("expires_in")
