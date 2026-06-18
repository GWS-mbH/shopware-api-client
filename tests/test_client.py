import asyncio
import logging
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from typing import Tuple
from unittest.mock import AsyncMock

import pytest
from httpx2 import AsyncClient, Response
from pytest_mock import MockerFixture

from shopware_api_client.base import (
    HEADER_X_RATE_LIMIT_LIMIT,
    HEADER_X_RATE_LIMIT_REMAINING,
    HEADER_X_RATE_LIMIT_RESET,
    RETRY_CACHE_KEY,
)
from shopware_api_client.cache import DictCache
from shopware_api_client.client import AdminClient, ClientBase, StoreClient
from shopware_api_client.config import AdminConfig, ConfigBase, StoreConfig
from shopware_api_client.exceptions import (
    SWAPIConfigException,
    SWAPIDataValidationError,
    SWAPIError,
    SWAPITooManyRequests,
)


@pytest.fixture
def rate_limit_headers():
    def _rate_limit_headers(remaining: int, reset: int | None, now: datetime = datetime.now()):
        headers = {
            "Date": now.strftime("%a, %d %b %Y %H:%M:%S"),
            HEADER_X_RATE_LIMIT_LIMIT: "1",
            HEADER_X_RATE_LIMIT_REMAINING: f"{remaining}",
        }

        if reset is not None:
            headers[HEADER_X_RATE_LIMIT_RESET] = str(int(now.timestamp()) + reset)

        return headers

    return _rate_limit_headers


@pytest.fixture
def patch_request(mocker: MockerFixture):
    def _patch(status: int, content: str = "", headers: dict[str, str] = {}) -> None:
        mocker.patch.object(
            AsyncClient,
            "request",
            AsyncMock(
                return_value=Response(
                    status_code=status,
                    content=content,
                    headers=headers,
                )
            ),
        )

    return _patch


@pytest.fixture
def patch_requests(mocker: MockerFixture):
    def _patch(response_contents: list[Tuple[int, str, dict[str, str]]]) -> None:
        responses = []
        for status, content, headers in response_contents:
            responses.append(Response(status_code=status, content=content, headers=headers))

        mocker.patch.object(AsyncClient, "request", AsyncMock(side_effect=responses))

    return _patch


class TestClientBase:
    def _get_http_client(self) -> AsyncClient:
        return AsyncClient()

    async def fake_sleep(self, _) -> None:
        self.sleep_hitcount += 1
        return None

    async def fake_cache_delete(self, key: str) -> None:
        return None

    async def assert_cached_reset_timestamp(self, now: datetime, wait_time: int) -> None:
        # Take rounding differences into account
        is_equal = int(now.timestamp()) + wait_time == await self.client.cache.get(self.reset_key) or int(
            now.timestamp()
        ) + wait_time + 1 == await self.client.cache.get(self.reset_key)
        assert is_equal, "Reset time was not cached properly"

    def setup_method(self) -> None:
        self.url = "https://localhost"
        self.relative_url = "/test"
        self.method = "get"
        self.base_config = ConfigBase(url=self.url, retry_after_threshold=10)
        self.client = ClientBase(config=self.base_config)
        self.client._get_http_client = self._get_http_client
        self.cache_key_base = RETRY_CACHE_KEY.format(
            url=self.url.removeprefix("https://") + self.relative_url, method=self.method
        )
        self.retry_lock_key = self.cache_key_base + ":lock"
        self.limit_key = self.cache_key_base + ":limit"
        self.remaining_key = self.cache_key_base + ":remaining"
        self.reset_key = self.cache_key_base + ":reset"
        self.sleep_hitcount = 0

    def test_get_header_ts(self, monkeypatch) -> None:
        standard_time = 1_111_111_111.11
        monkeypatch.setattr("shopware_api_client.base.time", lambda: standard_time)

        header_aware = "Tue, 15 Nov 1994 08:12:31 -0500"
        expected_ts = parsedate_to_datetime(header_aware).timestamp()
        actual_ts = self.client.get_header_ts(header_aware, standard_time)
        assert actual_ts == expected_ts, "The Date header with timezone did not parse correctly"

        header_naive = "Tue, 15 Nov 1994 08:12:31"
        expected_ts = parsedate_to_datetime(header_naive).replace(tzinfo=timezone.utc).timestamp()
        actual_ts = self.client.get_header_ts(header_naive, standard_time)
        assert actual_ts == expected_ts, "The Date header without timezone did not parse correctly"

        assert int(standard_time * 100) == int(self.client.get_header_ts(None, standard_time) * 100), (
            "Did not return the current time when Date header was missing"
        )

    def test_parse_reset_time(self, rate_limit_headers) -> None:
        response = Response(status_code=200, headers=rate_limit_headers(remaining=0, reset=45))
        assert 45 == self.client.parse_reset_time(response.headers), (
            f"Parsing {HEADER_X_RATE_LIMIT_RESET} was not successful"
        )

        response = Response(status_code=200, headers=rate_limit_headers(remaining=0, reset=-45))
        assert 0 == self.client.parse_reset_time(response.headers), (
            f"Parsing {HEADER_X_RATE_LIMIT_RESET} was not successful"
        )

    def test_parse_retry_after(self) -> None:
        response = Response(status_code=429)
        assert 1 == self.client.parse_retry_after(response.headers), "Missing Retry-After header did not return 1"

        response = Response(status_code=429, headers={"Retry-After": "0"})
        assert 1 == self.client.parse_retry_after(response.headers), (
            "Retry-After header of 0 did not result in returning 1"
        )

        response = Response(status_code=200, headers={"Retry-After": "5"})
        assert 5 == self.client.parse_retry_after(response.headers), (
            "Missing Retry-After header did not parse int correctly"
        )

        now = datetime.now()
        headers = {
            "Retry-After": (now + timedelta(seconds=10)).strftime("%a, %d %b %Y %H:%M:%S"),
            "Date": now.strftime("%a, %d %b %Y %H:%M:%S"),
        }
        response = Response(status_code=200, headers=headers)
        assert 10 == self.client.parse_retry_after(response.headers), (
            "Missing Retry-After header did not parse date format correctly"
        )

        headers.update(
            {
                "Retry-After": (now - timedelta(seconds=10)).strftime("%a, %d %b %Y %H:%M:%S"),
            }
        )
        response = Response(status_code=200, headers=headers)
        assert 1 == self.client.parse_retry_after(response.headers), (
            "Negative time-delay from Retry-After header did not result in returning 1"
        )

    async def test_429_retry(self, patch_requests, monkeypatch) -> None:
        wait_time = 9
        patch_requests([(429, "", {"Retry-After": f"{wait_time}"}), (200, "1", "")])
        monkeypatch.setattr("shopware_api_client.base.asyncio.sleep", self.fake_sleep)

        task = asyncio.create_task(self.client._make_request(self.method, self.relative_url, retries=1))

        result = await task
        assert 1 == result.json(), "Request did not succeed"
        assert 1 == self.sleep_hitcount, "Request did not wait even though it should have"

    async def test_429_retry_raises_without_retries(self, patch_request) -> None:
        patch_request(status=429, content="{}", headers={"Retry-After": "60"})

        with pytest.raises(SWAPITooManyRequests) as exc_info:
            await self.client._make_request(self.method, self.relative_url, retries=0)

        assert exc_info.value.headers["Retry-After"] == "60", "Retry-After header was not included in exception"


class TestAdminClient:
    def setup_method(self) -> None:
        self.admin_config = AdminConfig(
            url="https://localhost",
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
            grant_type="client_credentials",
            retry_after_threshold=10,
        )

    async def test_json_decode_error_with_200_response(self, patch_request) -> None:
        patch_request(
            status=200, content="read error", headers={"x-trace-id": "bla", "content-type": "application/json"}
        )

        client = AdminClient(config=self.admin_config)
        with pytest.raises(SWAPIError) as exc_info:
            await client.cms_page.all()

        exc: SWAPIError = exc_info.value
        assert exc.status == 500
        assert exc.title == "Internal Server Error"
        assert "x-trace-id" in exc.headers
        assert "bla" in exc.detail

    def test_creation(self) -> None:
        client = AdminClient(config=self.admin_config)
        assert isinstance(client, AdminClient)

    def test_get_client(self) -> None:
        client = AdminClient(config=self.admin_config)
        httpx_client = client.http_client
        assert isinstance(httpx_client, AsyncClient)

    def test_wrong_config(self) -> None:
        self.admin_config.client_id = None
        client = AdminClient(config=self.admin_config)
        httpx_client = None

        with pytest.raises(SWAPIConfigException):
            httpx_client = client.http_client

        assert httpx_client is None

    async def test_error_on_invalid_data_from_shopware(self, patch_request, caplog: pytest.LogCaptureFixture) -> None:
        caplog.set_level(logging.ERROR)
        patch_request(status=200, content='[{"id":1},{},{"id":3}]')

        client = AdminClient(config=self.admin_config)
        with pytest.raises(SWAPIDataValidationError) as exc_info:
            await client.cms_page.all()

        assert len(exc_info.value.errors) == 3
        assert len(caplog.records) == 3
        assert caplog.records[0].id == 1
        assert caplog.records[1].id is None
        assert caplog.records[2].id == 3

    async def test_load_custom_entities(self, mocker: MockerFixture) -> None:
        shared_cache = DictCache(cleanup_cycle_seconds=10)
        first_config = AdminConfig(
            url=self.admin_config.url,
            client_id=self.admin_config.client_id,
            client_secret=self.admin_config.client_secret,
            grant_type=self.admin_config.grant_type,
            cache=shared_cache,
        )
        second_config = AdminConfig(
            url=self.admin_config.url,
            client_id=self.admin_config.client_id,
            client_secret=self.admin_config.client_secret,
            grant_type=self.admin_config.grant_type,
            cache=shared_cache,
        )

        client = AdminClient(config=first_config)
        custom_entity_endpoint = client.custom_entity
        custom_entity = {
            "name": "my_custom_entity",
            "fields": [
                {"name": "required_int", "type": "int", "required": True},
                {"name": "optional_bool", "type": "bool", "required": False},
                {"name": "reference", "type": "many-to-one", "required": False},
                {"name": "children", "type": "one-to-many", "required": False},
            ],
        }

        async def fake_iter():
            yield custom_entity

        iter_mock = mocker.patch.object(type(custom_entity_endpoint), "iter", return_value=fake_iter())
        cache_key = f"custom_entities:{client.api_url}"

        await client.load_custom_entities()
        await client.load_custom_entities()

        assert await shared_cache.get(cache_key) == [custom_entity]

        second_client = AdminClient(config=second_config)
        await second_client.load_custom_entities()

        assert client.custom_entities_loaded is True
        assert iter_mock.call_count == 1
        assert hasattr(client, "my_custom_entity")
        assert second_client.custom_entities_loaded is True
        assert hasattr(second_client, "my_custom_entity")

        endpoint = client.my_custom_entity
        assert endpoint.client is client
        assert endpoint.name == "my_custom_entity"
        assert endpoint.path == "/my-custom-entity"
        assert endpoint.model_class._identifier.get_default() == "my_custom_entity"
        iter_mock.assert_called_once_with(raw=True)
        assert iter_mock.call_count == 1

        model_fields = endpoint.model_class.model_fields
        assert model_fields["required_int"].is_required()
        assert model_fields["optional_bool"].default is None
        assert model_fields["reference_id"].default is None
        assert "children" not in model_fields

        second_endpoint = second_client.my_custom_entity
        assert second_endpoint.client is second_client
        assert second_endpoint.path == "/my-custom-entity"
        assert second_endpoint.model_class._identifier.get_default() == "my_custom_entity"


class TestStoreClient:
    def setup_method(self) -> None:
        self.store_config = StoreConfig(url="https://localhost", access_key="ACCESS_KEY", retry_after_threshold=10)

    def test_creation(self) -> None:
        client = StoreClient(config=self.store_config)
        assert isinstance(client, StoreClient)

    def test_get_client(self) -> None:
        client = StoreClient(config=self.store_config)
        httpx_client = client.http_client
        assert isinstance(httpx_client, AsyncClient)

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
