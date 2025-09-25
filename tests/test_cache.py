import asyncio
import json
from typing import AsyncGenerator

import fakeredis
import pytest

from shopware_api_client.cache import CacheBase, DictCache, RedisCache


@pytest.fixture(params=["DictCache", "RedisCache"])
async def cache(request) -> AsyncGenerator[CacheBase, None]:
    match request.param:
        case "DictCache":
            yield DictCache(cleanup_cycle_seconds=1)

        case "RedisCache":
            redis = fakeredis.aioredis.FakeRedis()
            yield RedisCache(redis)
            await redis.flushdb()

        case other:
            raise ValueError(f"Unknown cache type: {other!r}")


class TestCaches:
    test_key = "key"

    @pytest.mark.asyncio
    async def test_set_and_get(self, cache: CacheBase) -> None:
        test_data = {
            "1": {"a": 1},
            "2": [1, 2],
            "3": 1,
            "4": "string",
            "5": True,
        }

        for k, v in test_data.items():
            await cache.set(k, v)
            assert await cache.get(k) == v, "Set or get was not successful"

    @pytest.mark.asyncio
    async def test_get_and_decrement(self, cache: CacheBase) -> None:
        no_value = await cache.get_and_decrement(self.test_key)
        assert no_value is None, "Decrementing missing key did not return None"

        counter = 4
        await cache.set(self.test_key, counter)
        for _ in reversed(range(counter * 2)):
            return_value = await cache.get_and_decrement(self.test_key)
            assert return_value == counter, "Decrement was not successful"
            counter -= 1

    @pytest.mark.asyncio
    async def test_delete(self, cache: CacheBase) -> None:
        await cache.set(self.test_key, 123)
        await cache.delete(self.test_key)
        assert await cache.get(self.test_key) is None, "Key was not deleted"
        await cache.delete(self.test_key)
        assert await cache.get(self.test_key) is None, "Delete on missing key failed"

    @pytest.mark.asyncio
    async def test_has_lock(self, cache: CacheBase) -> None:
        has_lock_1 = await cache.has_lock(self.test_key, ttl=10)
        assert has_lock_1 is True, "First has_lock should succeed"

        has_lock_2 = await cache.has_lock(self.test_key, ttl=10)
        assert has_lock_2 is False, "Second has_lock should fail while lock exists"

        await cache.delete(self.test_key)
        has_lock_3 = await cache.has_lock(self.test_key, ttl=10)
        assert has_lock_3 is True, "After delete, has_lock should succeed again"

    @pytest.mark.asyncio
    async def test_ttls(self, cache: CacheBase) -> None:
        key_lock = "key_lock"
        key_set = "key_set"

        await asyncio.gather(cache.set(key_set, key_set, 1), cache.has_lock(key_lock, 1), asyncio.sleep(1.1))

        assert await cache.get(key_set) is None
        assert await cache.get(key_lock) is None

    def test_json_encode_decode(self, cache: CacheBase) -> None:
        for value in (1, "1", [1, "1"], {"1": 1, "2": 1}, None):
            encoded_value = cache._json_encode(self.test_key, value)
            assert encoded_value == json.dumps(value), "JSON-encoding failed"
            decoded_value = cache._json_decode(encoded_value)
            assert value == decoded_value

        assert cache._json_decode(None) is None
        assert cache._json_decode("Invalid JSON") is None

        with pytest.raises(ValueError):
            cache._json_encode(self.test_key, {1, 2})
