import pytest
from shopware_api_client import client as api_client
from shopware_api_client.base import ApiModelBase, EndpointBase
from shopware_api_client.client import AdminClient, EndpointRegistry, StoreClient
from shopware_api_client.config import AdminConfig, StoreConfig


class SomeModel(ApiModelBase["SomeModelEndpoint"]):
    _identifier = "some_model"

    name: str | None = None


class SomeModelEndpoint(EndpointBase[SomeModel]):
    name = "some_model"
    path = "/some-model"
    model_class = SomeModel


class TestRegistry:
    def setup_method(self) -> None:
        self.admin_config = AdminConfig(
            url="https://localhost",
            client_id="CLIENT_ID",
            client_secret="CLIENT_SECRET",
            grant_type="client_credentials",
        )
        self.store_config = StoreConfig(url="https://localhost", access_key="ACCESS_KEY")
        api_client.registry = EndpointRegistry()

    def test_register_admin(self) -> None:
        client = AdminClient(config=self.admin_config)

        assert hasattr(client, "some_model") is False

        api_client.registry.register_admin(SomeModelEndpoint)
        client = AdminClient(config=self.admin_config)

        assert hasattr(client, "some_model")

    def test_register_store(self) -> None:
        client = StoreClient(config=self.store_config)

        assert hasattr(client, "some_model") is False

        api_client.registry.register_store(SomeModelEndpoint)
        client = StoreClient(config=self.store_config)

        assert hasattr(client, "some_model")

    def test_get_admin_model(self) -> None:
        with pytest.raises(KeyError):
            api_client.registry.get_admin_model("SomeModel")

        api_client.registry.register_admin(SomeModelEndpoint)

        model_class = api_client.registry.get_admin_model("SomeModel")

        assert model_class == SomeModel

    def test_get_store_model(self) -> None:
        with pytest.raises(KeyError):
            api_client.registry.get_store_model("SomeModel")

        api_client.registry.register_store(SomeModelEndpoint)

        model_class = api_client.registry.get_store_model("SomeModel")

        assert model_class == SomeModel
