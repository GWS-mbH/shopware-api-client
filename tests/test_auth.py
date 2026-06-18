from unittest.mock import AsyncMock, Mock

import pytest
from httpx2 import AsyncClient, Request
from pytest_mock import MockerFixture

from shopware_api_client.auth import ShopwareAdminAPIAuth, ShopwareAdminPasswordAPIAuth
from shopware_api_client.config import AdminConfig


@pytest.fixture
def patch_oauth_post(mocker: MockerFixture):
    def _patch(response: Mock) -> AsyncMock:
        post_mock = AsyncMock(return_value=response)
        mocker.patch.object(AsyncClient, "post", post_mock)
        return post_mock

    return _patch


class TestShopwareAdminAPIAuth:
    def setup_method(self) -> None:
        self.config = AdminConfig(
            url="https://localhost",
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
            grant_type="client_credentials",
            extra={"audience": "admin-api"},
        )
        self.auth = ShopwareAdminAPIAuth(config=self.config)

    async def test_get_access_token_from_shopware_success(self, patch_oauth_post) -> None:
        response = Mock()
        response.raise_for_status = Mock()
        response.json = Mock(return_value={"access_token": "TOKEN_1", "expires_in": 120})
        post_mock = patch_oauth_post(response)

        token, expires_in = await self.auth._get_access_token_from_shopware()

        assert token == "TOKEN_1"
        assert expires_in == 120
        post_mock.assert_called_once_with(
            self.auth.auth_url,
            data={
                "client_id": "CLIENT_ID",
                "client_secret": "CLIENT_SECRET",
                "grant_type": "client_credentials",
                "audience": "admin-api",
            },
        )

    async def test_get_access_token_from_shopware_error(self, patch_oauth_post) -> None:
        class OAuthError(Exception):
            pass

        response = Mock()
        response.raise_for_status = Mock(side_effect=OAuthError("oauth failed"))
        response.json = Mock(return_value={})
        patch_oauth_post(response)

        with pytest.raises(OAuthError, match="oauth failed"):
            await self.auth._get_access_token_from_shopware()

    async def test_get_access_token_uses_cache(self, mocker: MockerFixture) -> None:
        await self.config.cache.set(self.auth._cache_key, "CACHED_TOKEN")
        fetch_mock = mocker.patch.object(self.auth, "_get_access_token_from_shopware", AsyncMock())

        token = await self.auth._get_access_token()

        assert token == "CACHED_TOKEN"
        fetch_mock.assert_not_called()

    async def test_get_access_token_fetches_oauth_when_cache_miss(self, mocker: MockerFixture) -> None:
        fetch_mock = mocker.patch.object(
            self.auth,
            "_get_access_token_from_shopware",
            AsyncMock(return_value=("FRESH_TOKEN", 300)),
        )

        token = await self.auth._get_access_token()

        assert token == "FRESH_TOKEN"
        fetch_mock.assert_awaited_once()

    async def test_async_auth_flow_adds_bearer_header(self, mocker: MockerFixture) -> None:
        mocker.patch.object(self.auth, "_get_access_token", AsyncMock(return_value="FLOW_TOKEN"))
        request = Request("GET", "https://localhost/api/test")

        auth_flow = self.auth.async_auth_flow(request)
        authenticated_request = await anext(auth_flow)

        assert authenticated_request.headers["Authorization"] == "Bearer FLOW_TOKEN"


class TestShopwareAdminPasswordAPIAuth:
    def setup_method(self) -> None:
        self.config = AdminConfig(
            url="https://localhost",
            username="admin",
            password="secret",
            grant_type="password",
            extra={"scope_hint": "all"},
        )
        self.auth = ShopwareAdminPasswordAPIAuth(config=self.config)

    async def test_get_access_token_from_shopware_success(self, patch_oauth_post) -> None:
        response = Mock()
        response.raise_for_status = Mock()
        response.json = Mock(return_value={"access_token": "TOKEN_2", "expires_in": 90})
        post_mock = patch_oauth_post(response)

        token, expires_in = await self.auth._get_access_token_from_shopware()

        assert token == "TOKEN_2"
        assert expires_in == 90
        post_mock.assert_called_once_with(
            self.auth.auth_url,
            data={
                "client_id": "administration",
                "scopes": "write",
                "grant_type": "password",
                "username": "admin",
                "password": "secret",
                "scope_hint": "all",
            },
        )

    async def test_get_access_token_from_shopware_error(self, patch_oauth_post) -> None:
        class OAuthError(Exception):
            pass

        response = Mock()
        response.raise_for_status = Mock(side_effect=OAuthError("oauth failed"))
        response.json = Mock(return_value={})
        patch_oauth_post(response)

        with pytest.raises(OAuthError, match="oauth failed"):
            await self.auth._get_access_token_from_shopware()

    async def test_get_access_token_uses_cache(self, mocker: MockerFixture) -> None:
        await self.config.cache.set(self.auth._cache_key, "CACHED_PASSWORD_TOKEN")
        fetch_mock = mocker.patch.object(self.auth, "_get_access_token_from_shopware", AsyncMock())

        token = await self.auth._get_access_token()

        assert token == "CACHED_PASSWORD_TOKEN"
        fetch_mock.assert_not_called()

    async def test_get_access_token_fetches_oauth_when_cache_miss(self, mocker: MockerFixture) -> None:
        fetch_mock = mocker.patch.object(
            self.auth,
            "_get_access_token_from_shopware",
            AsyncMock(return_value=("FRESH_PASSWORD_TOKEN", 300)),
        )

        token = await self.auth._get_access_token()

        assert token == "FRESH_PASSWORD_TOKEN"
        fetch_mock.assert_awaited_once()

    async def test_async_auth_flow_adds_bearer_header(self, mocker: MockerFixture) -> None:
        mocker.patch.object(self.auth, "_get_access_token", AsyncMock(return_value="FLOW_PASSWORD_TOKEN"))
        request = Request("GET", "https://localhost/api/test")

        auth_flow = self.auth.async_auth_flow(request)
        authenticated_request = await anext(auth_flow)

        assert authenticated_request.headers["Authorization"] == "Bearer FLOW_PASSWORD_TOKEN"
