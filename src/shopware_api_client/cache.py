import json
from collections import OrderedDict
from time import time
from typing import Any, NamedTuple, Protocol


class CacheProtocol(Protocol):
    async def get(self, key: str) -> Any | None: ...

    async def set(self, key: str, value: Any, ttl: int | None = None) -> None: ...

    async def delete(self, key: str) -> None: ...


class DictCache(CacheProtocol):
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

    def _json_encode(self, key: str, value: Any) -> str:
        try:
            return json.dumps(value)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Value {value!r} for cache key {key!r} must be JSON-serializable: {e}") from e

    def _json_decode(self, raw_value: Any) -> Any | None:
        if raw_value is None:
            return None

        try:
            return json.loads(raw_value)
        except json.JSONDecodeError:
            # If write was broken, mimic missing key
            return None
