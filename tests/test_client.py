import logging
from unittest.mock import AsyncMock

import httpx
import pytest
from pytest_mock import MockerFixture

from shopware_api_client.client import AdminClient, StoreClient
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
                return_value=httpx.Response(status_code=200, content="read error", headers={"x-trace-id": "bla"})
            ),
        )
        client = AdminClient(config=self.admin_config)
        with pytest.raises(SWAPIError) as exc_info:
            await client.cms_page.all()

        exc: SWAPIError = exc_info.value
        assert exc.status == 500
        assert exc.title == "Internal Server Error"
        assert "bla" in exc.detail

    def test_creation(self) -> None:
        client = AdminClient(config=self.admin_config)
        assert isinstance(client, AdminClient)

    def test_get_client(self) -> None:
        client = AdminClient(config=self.admin_config)
        httpx_client = client.http_client
        assert isinstance(httpx_client, httpx.AsyncClient)

    def test_wrong_config(self) -> None:
        self.admin_config.client_id = None
        client = AdminClient(config=self.admin_config)

        with pytest.raises(SWAPIConfigException):
            client.http_client

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


class TestStoreClient:
    def setup_method(self) -> None:
        self.store_config = StoreConfig(url="https://localhost", access_key="ACCESS_KEY")

    def test_creation(self) -> None:
        client = StoreClient(config=self.store_config)
        assert isinstance(client, StoreClient)

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
