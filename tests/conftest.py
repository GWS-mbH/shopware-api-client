import fakeredis
import pytest


@pytest.fixture
def redis_client():
    redis_client = fakeredis.FakeRedis()
    return redis_client
