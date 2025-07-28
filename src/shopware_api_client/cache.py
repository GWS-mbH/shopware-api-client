import json
from abc import ABC, abstractmethod
from collections import OrderedDict
from time import time
from typing import Any, Awaitable, NamedTuple, cast

try:
    from redis.asyncio import Redis

    _has_redis = True
except ModuleNotFoundError:
    _has_redis = False


class CacheBase(ABC):
    @abstractmethod
    async def get(self, key: str) -> Any | None:
        ...

    @abstractmethod
    async def get_and_decrement(self, key: str) -> int | None:
        ...

    @abstractmethod
    async def has_lock(self, key: str, ttl: int) -> bool:
        ...

    @abstractmethod
    async def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        ...

    @abstractmethod
    async def delete(self, key: str) -> None:
        ...

    @staticmethod
    def _json_encode(key: str, value: Any) -> str:
        try:
            return json.dumps(value)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Value {value!r} for cache key {key!r} must be JSON-serializable: {e}") from e

    @staticmethod
    def _json_decode(raw_value: Any) -> Any | None:
        if raw_value is None:
            return None

        try:
            return json.loads(raw_value)
        except json.JSONDecodeError:
            # If write was broken, mimic missing key
            return None


class RedisCache(CacheBase):
    _DECR_IF_EXISTS = """
        if redis.call('EXISTS', KEYS[1]) == 1 then
            return redis.call('DECR', KEYS[1])
        else
            return nil
        end
    """

    def __init__(self, redis_client: "Redis") -> None:
        if not _has_redis:
            raise RuntimeError("Redis needs to be installed to use it as a cache.")

        self.client = redis_client

    async def get(self, key: str) -> Any | None:
        value = await self.client.get(key)
        return self._json_decode(value)

    async def get_and_decrement(self, key: str) -> int | None:
        return_value = await cast(Awaitable[int | None], self.client.eval(self._DECR_IF_EXISTS, 1, key))
        return None if return_value is None else return_value + 1

    async def has_lock(self, key: str, ttl: int) -> bool:
        return await self.client.set(key, 1, ex=ttl, nx=True) or False

    async def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        await self.client.set(name=key, value=self._json_encode(key, value), ex=ttl)

    async def delete(self, key: str) -> None:
        await self.client.delete(key)


class DictCache(CacheBase):
    class CacheValue(NamedTuple):
        value: Any
        expire_at: int | None

    def __init__(self, cleanup_cycle_seconds: int) -> None:
        self._cache: OrderedDict[str, DictCache.CacheValue] = OrderedDict()
        self.cleanup_cycle_seconds = cleanup_cycle_seconds
        self.next_cleanup: int = 0

    async def get(self, key: str) -> Any | None:
        self._cleanup_by_expiry()
        entry = self._cache.get(key)

        return self._json_decode(entry and entry.value)

    async def get_and_decrement(self, key: str) -> int | None:
        self._cleanup_by_expiry()
        entry = self._cache.get(key)
        if entry is None:
            return None

        decoded_value = self._json_decode(entry.value)
        if not isinstance(decoded_value, int):
            raise ValueError(f"Trying to decrement key {key!r}, but value {decoded_value!r} is not an int")

        new_value = decoded_value - 1
        self._cache[key] = DictCache.CacheValue(self._json_encode(key, new_value), entry.expire_at)

        return decoded_value

    async def has_lock(self, key: str, ttl: int) -> bool:
        self._cleanup_by_expiry(False)
        entry = self._cache.get(key)
        if unlocked := entry is None:
            self._cache[key] = DictCache.CacheValue(True, self.get_expiry(ttl))

        return unlocked

    async def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        self._cleanup_by_expiry()
        cache_value = self._json_encode(key, value)

        self._cache[key] = DictCache.CacheValue(cache_value, self.get_expiry(ttl))

    async def delete(self, key: str) -> None:
        self._cleanup_by_expiry()
        self._cache.pop(key, None)

    def get_expiry(self, ttl: int | None) -> int | None:
        return int(time()) + ttl if ttl is not None else None

    def _cleanup_by_expiry(self, do_wait: bool = True) -> None:
        now = int(time())

        if now < self.next_cleanup and do_wait:
            return

        initial_size = len(self._cache)
        for _ in range(initial_size):
            if not self._cache:
                break

            first_key, first_value = next(iter(self._cache.items()))

            if first_value.expire_at is None:
                self._cache.move_to_end(first_key)
                continue

            if first_value.expire_at > now:
                break

            self._cache.popitem(last=False)

        self.next_cleanup = now + self.cleanup_cycle_seconds
