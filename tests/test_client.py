import asyncio
import logging
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from typing import Tuple
from unittest.mock import AsyncMock

import httpx
import pytest
from pytest_mock import MockerFixture

from shopware_api_client.base import (
    HEADER_X_RATE_LIMIT_LIMIT,
    HEADER_X_RATE_LIMIT_REMAINING,
    HEADER_X_RATE_LIMIT_RESET,
    RETRY_CACHE_KEY,
)
from shopware_api_client.client import AdminClient, ClientBase, StoreClient
from shopware_api_client.config import AdminConfig, ConfigBase, StoreConfig
from shopware_api_client.exceptions import (
    SWAPIConfigException,
    SWAPIDataValidationError,
    SWAPIError,
    SWAPIRetryException,
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
        mocker.patch(
            "httpx.AsyncClient.request",
            AsyncMock(
                return_value=httpx.Response(
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
            responses.append(httpx.Response(status_code=status, content=content, headers=headers))

        mocker.patch("httpx.AsyncClient.request", AsyncMock(side_effect=responses))

    return _patch


class TestClientBase:
    def _get_http_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient()

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
        self.base_config = ConfigBase(
            url=self.url,
            retry_after_threshold=10,
            local_cache_cleanup_cycle_seconds=10,
        )
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

        assert int(standard_time * 100) == int(
            self.client.get_header_ts(None, standard_time) * 100
        ), "Did not return the current time when Date header was missing"

    def test_parse_reset_time(self, rate_limit_headers) -> None:
        response = httpx.Response(status_code=200, headers=rate_limit_headers(remaining=0, reset=45))
        assert 45 == self.client.parse_reset_time(
            response.headers
        ), f"Parsing {HEADER_X_RATE_LIMIT_RESET} was not successful"

        response = httpx.Response(status_code=200, headers=rate_limit_headers(remaining=0, reset=-45))
        assert 0 == self.client.parse_reset_time(
            response.headers
        ), f"Parsing {HEADER_X_RATE_LIMIT_RESET} was not successful"

    def test_parse_retry_after(self) -> None:
        response = httpx.Response(status_code=429)
        assert 1 == self.client.parse_retry_after(response.headers), "Missing Retry-After header did not return 1"

        response = httpx.Response(status_code=429, headers={"Retry-After": "0"})
        assert 1 == self.client.parse_retry_after(
            response.headers
        ), "Retry-After header of 0 did not result in returning 1"

        response = httpx.Response(status_code=200, headers={"Retry-After": "5"})
        assert 5 == self.client.parse_retry_after(
            response.headers
        ), "Missing Retry-After header did not parse int correctly"

        now = datetime.now()
        headers = {
            "Retry-After": (now + timedelta(seconds=10)).strftime("%a, %d %b %Y %H:%M:%S"),
            "Date": now.strftime("%a, %d %b %Y %H:%M:%S"),
        }
        response = httpx.Response(status_code=200, headers=headers)
        assert 10 == self.client.parse_retry_after(
            response.headers
        ), "Missing Retry-After header did not parse date format correctly"

        headers.update(
            {
                "Retry-After": (now - timedelta(seconds=10)).strftime("%a, %d %b %Y %H:%M:%S"),
            }
        )
        response = httpx.Response(status_code=200, headers=headers)
        assert 1 == self.client.parse_retry_after(
            response.headers
        ), "Negative time-delay from Retry-After header did not result in returning 1"

    async def test_x_rate_limit_retry(self, patch_request, rate_limit_headers, monkeypatch) -> None:
        now = datetime.now()
        wait_time = 9
        patch_request(status=200, content="1", headers=rate_limit_headers(remaining=0, reset=wait_time, now=now))
        monkeypatch.setattr("shopware_api_client.base.asyncio.sleep", self.fake_sleep)

        result_count = 0

        response_1 = await self.client._make_request(self.method, self.relative_url)
        result_count += response_1.json()
        assert result_count == 1, "First request did not succeeded"
        assert self.sleep_hitcount == 0, "Request waited even though it shouldn't"

        response_2 = asyncio.create_task(self.client._make_request(self.method, self.relative_url))
        try:
            result = await asyncio.wait_for(response_2, 1)
        except asyncio.TimeoutError:
            raise AssertionError("_make_request is expected to return almost instantaneously in this test")

        result_count += result.json()
        assert result_count == 2, "Second request did not succeeded"
        assert self.sleep_hitcount == 1, "Request did not wait even though it should have"

        assert await self.client.cache.has_lock(self.retry_lock_key, 1) is True, "Key was not released properly"
        await self.client.cache.delete(self.retry_lock_key)

        self.client.cache.delete = self.fake_cache_delete
        response_3 = await self.client._make_request(self.method, self.relative_url)
        result_count += response_3.json()
        assert result_count == 3, "Third request did not succeeded"
        assert self.sleep_hitcount == 2, "Request did not wait even though it should have"

        assert await self.client.cache.has_lock(self.retry_lock_key, 1) is False, "Key has not been taken properly"

        attempts = (asyncio.create_task(self.client._make_request(self.method, self.relative_url)) for _ in range(10))
        for attempt in attempts:
            assert attempt.done() is False, "Request is not waiting even though key is taken"
            attempt.cancel()
        assert result_count == 3, "Requests got through even though all should be in back-off loop"

        assert 1 == await self.client.cache.get(self.limit_key), "Limit was not cached properly"
        assert 0 == await self.client.cache.get(self.remaining_key), "Remaining requests were not cached properly"
        await self.assert_cached_reset_timestamp(now, wait_time)

    async def test_x_rate_limit_retry_0_reset_time(self, patch_request, rate_limit_headers) -> None:
        patch_request(status=200, content="{}", headers=rate_limit_headers(remaining=1, reset=0))
        await self.client._make_request(self.method, self.relative_url)
        assert (
            self.client.cache._cache.get(self.reset_key) is None  # type: ignore
        ), f"Cache key was set for {self.reset_key!r} but it shouldn't be set"

        patch_request(status=200, content="{}", headers=rate_limit_headers(remaining=0, reset=None))
        await self.client._make_request(self.method, self.relative_url)
        assert (
            self.client.cache._cache.get(self.reset_key) is None  # type: ignore
        ), f"Cache key was set for {self.reset_key!r} but it shouldn't be set"

    async def test_x_rate_limit_retry_threshold(self, patch_request, rate_limit_headers) -> None:
        patch_request(status=200, content="{}", headers=rate_limit_headers(remaining=0, reset=60))

        await self.client._make_request(self.method, self.relative_url)
        with pytest.raises(SWAPIRetryException):
            await self.client._make_request(self.method, self.relative_url)

    async def test_429_retry(self, patch_requests, monkeypatch) -> None:
        now = datetime.now()
        wait_time = 9
        patch_requests([(429, "", {"Retry-After": f"{wait_time}"}), (200, "1", "")])
        monkeypatch.setattr("shopware_api_client.base.asyncio.sleep", self.fake_sleep)

        task = asyncio.create_task(self.client._make_request(self.method, self.relative_url))

        result = await task
        assert 1 == result.json(), "Request did not succeed"
        assert 1 == self.sleep_hitcount, "Request did not wait even though it should have"
        await self.assert_cached_reset_timestamp(now, wait_time)

    async def test_429_retry_threshold(self, patch_request) -> None:
        patch_request(status=429, content="{}", headers={"Retry-After": "60"})

        with pytest.raises(SWAPIRetryException):
            await self.client._make_request(self.method, self.relative_url)

    async def test_429_with_x_rate_limit_retry(self, patch_requests, rate_limit_headers, monkeypatch):
        now = datetime.now()
        monkeypatch.setattr("shopware_api_client.base.asyncio.sleep", self.fake_sleep)
        rl_headers = rate_limit_headers(remaining=0, reset=9, now=now)
        patch_requests([(200, "1", rl_headers), (429, "", {"Retry-After": "9"}), (200, "1", rl_headers)])

        result_1 = await self.client._make_request(self.method, self.relative_url)
        result_2 = await self.client._make_request(self.method, self.relative_url)

        assert 1 == result_1.json() == result_2.json(), "Requests did not succeed"
        assert 2 == self.sleep_hitcount, "Requests did not wait properly"


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
        assert exc.title == httpx.codes.get_reason_phrase(500)
        assert "x-trace-id" in exc.headers
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


class TestStoreClient:
    def setup_method(self) -> None:
        self.store_config = StoreConfig(url="https://localhost", access_key="ACCESS_KEY", retry_after_threshold=10)

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
