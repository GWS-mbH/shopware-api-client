import logging
from typing import cast
from unittest.mock import AsyncMock

import httpx
import pytest
from fakeredis import FakeRedis
from pytest_mock import MockerFixture

from shopware_api_client.client import AdminClient, OAuth2ClientCredentialsRedisCached, StoreClient
from shopware_api_client.config import AdminConfig, StoreConfig
from shopware_api_client.exceptions import SWAPIConfigException, SWAPIDataValidationError, SWAPIError


class TestAdminClient:
    def setup_method(self) -> None:
        self.admin_config = AdminConfig(
            url="https://localhost",
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
            grant_type="client_credentials",
        )

    async def test_json_decode_error_with_200_response(self, mocker: MockerFixture) -> None:
        mocker.patch(
            "httpx.AsyncClient.request",
            AsyncMock(
                return_value=httpx.Response(
                    status_code=200,
                    content="read error",
                    headers={"x-trace-id": "bla", "content-type": "application/json"},
                )
            ),
        )
        client = AdminClient(config=self.admin_config)
        with pytest.raises(SWAPIError) as exc_info:
            await client.cms_page.all()

        exc: SWAPIError = exc_info.value
        assert exc.status == 500
        assert exc.title == httpx.codes.get_reason_phrase(500)
        assert "x-trace-id" in exc.headers
        assert "bla" in exc.detail

    def test_creation(self) -> None:
        client = AdminClient(config=self.admin_config)
        assert isinstance(client, AdminClient)

    def test_instance(self) -> None:
        client = AdminClient.instance(config=self.admin_config)
        client2 = AdminClient.instance(config=self.admin_config)
        assert id(client) == id(client2)

    def test_get_client(self) -> None:
        client = AdminClient(config=self.admin_config)
        httpx_client = client.http_client
        assert isinstance(httpx_client, httpx.AsyncClient)

    def test_wrong_config(self) -> None:
        self.admin_config.client_id = None
        client = AdminClient(config=self.admin_config)
        httpx_client = None

        with pytest.raises(SWAPIConfigException):
            httpx_client = client.http_client

        assert httpx_client is None

    async def test_error_on_invalid_data_from_shopware(
        self, mocker: MockerFixture, caplog: pytest.LogCaptureFixture
    ) -> None:
        caplog.set_level(logging.ERROR)
        mocker.patch(
            "httpx.AsyncClient.request",
            AsyncMock(return_value=httpx.Response(status_code=200, content='[{"id":1},{},{"id":3}]')),
        )
        client = AdminClient(config=self.admin_config)
        with pytest.raises(SWAPIDataValidationError) as exc_info:
            await client.cms_page.all()

        assert len(exc_info.value.errors) == 3
        assert len(caplog.records) == 3
        assert caplog.records[0].id == 1
        assert caplog.records[1].id is None
        assert caplog.records[2].id == 3

    async def test_redis_cache(self, redis_client: FakeRedis):
        self.setup_method()
        self.admin_config.extra["redis_cache_client"] = redis_client

        #
        # test client setting up cache in httpx client
        #
        client = AdminClient.instance(config=self.admin_config)

        httpx_call_count = 0

        def httpx_mock_request(request):
            nonlocal httpx_call_count
            httpx_call_count += 1
            return httpx.Response(
                200,
                content='{"access_token": "test-token","token_type":"Bearer","expires_in":3600,"refresh_token":"refresh-token"}',
            )

        # mock httpx client
        client.httpx_init_kwargs["transport"] = httpx.MockTransport(httpx_mock_request)

        httpx_client = client.http_client
        assert isinstance(httpx_client.auth, OAuth2ClientCredentialsRedisCached)

        #
        # test cache
        #
        client_auth = cast(OAuth2ClientCredentialsRedisCached, client.http_client.auth)

        # add non-cached token
        request = httpx.Request("get", "/test")
        httpx_client = next(client_auth.auth_flow(request))
        assert httpx_call_count == 1
        assert request.headers.get(client_auth.header_name) == "Bearer test-token"

        # get cached token
        request = httpx.Request("get", "/test")
        httpx_client = next(client_auth.auth_flow(request))
        assert httpx_call_count == 1  # cached, should stay at 1
        assert request.headers.get(client_auth.header_name) == "Bearer test-token"


class TestStoreClient:
    def setup_method(self) -> None:
        self.store_config = StoreConfig(url="https://localhost", access_key="ACCESS_KEY")

    def test_creation(self) -> None:
        client = StoreClient(config=self.store_config)
        assert isinstance(client, StoreClient)

    def test_instance(self) -> None:
        client = StoreClient.instance(config=self.store_config)
        client2 = StoreClient.instance(config=self.store_config)
        assert id(client) == id(client2)

    def test_get_client(self) -> None:
        client = StoreClient(config=self.store_config)
        httpx_client = client.http_client
        assert isinstance(httpx_client, httpx.AsyncClient)

    def test_context_token(self) -> None:
        config = StoreConfig(url="https://localhost", access_key="ACCESS_KEY", context_token="CONTEXT_TOKEN")
        client = StoreClient(config=config)
        httpx_client = client.http_client
        headers = httpx_client.headers
        assert headers.get("sw-context-token") == "CONTEXT_TOKEN"

    def test_context_token_not_set(self) -> None:
        client = StoreClient(config=self.store_config)
        httpx_client = client.http_client
        headers = httpx_client.headers
        assert headers.get("sw-context-token") is None
