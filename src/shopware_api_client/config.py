from typing import Any

from .base import ConfigBase
from .exceptions import SWAPIConfigException


class AdminConfig(ConfigBase):
    def __init__(
        self,
        url: str,
        username: str | None = None,
        password: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        grant_type: str = "client_credentials",
        extra: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        match grant_type:
            case "client_credentials":
                if client_id is None or client_secret is None:
                    raise SWAPIConfigException(
                        "'client_id' and 'client_secret' must be set for grant_type 'client_credentials'"
                    )
            case "password":
                if username is None or password is None:
                    raise SWAPIConfigException("'username' and 'password' must be set for grant_type 'password'")
            case _:
                raise SWAPIConfigException("Invalid 'grant_type'. Must be one of: 'client_credentials', 'password'")

        super().__init__(url=url, **kwargs)
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.extra = extra or {}


class StoreConfig(ConfigBase):
    def __init__(self, url: str, access_key: str, context_token: str | None = None, **kwargs: Any):
        super().__init__(url=url, **kwargs)
        self.access_key = access_key
        self.context_token = context_token
