from typing import Generator

from httpx2 import Auth, Request, Response
from httpx2 import post as post_request

from shopware_api_client.base import ConfigBase
from shopware_api_client.config import AdminConfig
from shopware_api_client.exceptions import SWAPIException


class ShopwareAPIAuth(Auth):

    def __init__(self, config: ConfigBase):
        self.config = config


class ShopwareAdminAPIAuth(ShopwareAPIAuth):

    def __init__(self, config: AdminConfig):
        super().__init__(config)
        self.auth_url = f"{config.url}/api/oauth/token"

    def _get_access_token(self) -> str | None:
        assert isinstance(self.config, AdminConfig), "Config must be of type AdminConfig"

        payload = {
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "grant_type": "client_credentials"
        }
        response = post_request(self.auth_url, data=payload)
        response.raise_for_status()
        return response.json().get("access_token")

    def auth_flow(self, request: Request) -> Generator[Request, Response, None]:
        access_token = self._get_access_token()
        if not access_token:
            raise SWAPIException("Failed to obtain access token.")

        request.headers["Authorization"] = f"Bearer {access_token}"

        yield request


class ShopwareAdminPasswordAPIAuth(ShopwareAdminAPIAuth):

    def _get_access_token(self) -> str | None:
        assert isinstance(self.config, AdminConfig), "Config must be of type AdminConfig"

        payload = {
            "client_secret": self.config.client_secret,
            "grant_type": "password",
            "username": self.config.username,
            "password": self.config.password
        }
        response = post_request(self.auth_url, data=payload)
        response.raise_for_status()
        return response.json().get("access_token")
