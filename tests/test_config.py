import pytest
from shopware_api_client.config import AdminConfig, StoreConfig
from shopware_api_client.exceptions import SWAPIConfigException


class TestAdminConfig:
    URL = "https://localhost"
    CLIENT_ID = "CLIENT_ID"
    CLIENT_SECRET = "CLIENT_SECRET"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"

    def test_creation_client_credentials(self) -> None:
        config = AdminConfig(
            url=self.URL, client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, grant_type="client_credentials"
        )
        assert isinstance(config, AdminConfig)

    def test_creation_client_credentials_missing_param(self) -> None:
        with pytest.raises(SWAPIConfigException):
            AdminConfig(url=self.URL, client_id=self.CLIENT_ID, grant_type="client_credentials")

        with pytest.raises(SWAPIConfigException):
            AdminConfig(url=self.URL, client_secret=self.CLIENT_SECRET, grant_type="client_credentials")

    def test_creation_default_grant_type(self) -> None:
        config = AdminConfig(url=self.URL, client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET)
        assert isinstance(config, AdminConfig)
        assert config.grant_type == "client_credentials"

    def test_creation_password(self) -> None:
        config = AdminConfig(url=self.URL, username=self.USERNAME, password=self.PASSWORD, grant_type="password")

        assert isinstance(config, AdminConfig)

    def test_creation_password_missing_param(self) -> None:
        with pytest.raises(SWAPIConfigException):
            AdminConfig(url=self.URL, username=self.USERNAME, grant_type="password")

        with pytest.raises(SWAPIConfigException):
            AdminConfig(url=self.URL, password=self.PASSWORD)

    def test_creation_invalid_grant_type(self) -> None:
        with pytest.raises(SWAPIConfigException):
            AdminConfig(url=self.URL, grant_type="client")


class TestStoreCOnfig:
    URL = "https://localhost"
    ACCESS_KEY = "ACCESS_KEY"
    CONTEXT_TOKEN = "CONTEXT_TOKEN"

    def test_creation(self) -> None:
        config = StoreConfig(url=self.URL, access_key=self.ACCESS_KEY, context_token=self.CONTEXT_TOKEN)
        assert isinstance(config, StoreConfig)

    def test_creation_no_context(self) -> None:
        config = StoreConfig(url=self.URL, access_key=self.ACCESS_KEY)
        assert isinstance(config, StoreConfig)
