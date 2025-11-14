from typing import Any

from shopware_api_client.base import ClientBase, StoreSearchEndpoint, EndpointMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.models.country_state import CountryStateBase


class CountryState(CountryStateBase, EndpointMixin["CountryStateEndpoint"]):
    pass


class CountryStateEndpoint(StoreSearchEndpoint[CountryState]):
    model_class = CountryState
    name = "country_state"
    path = "/country-state/"

    def __init__(self, client: ClientBase, country_id: IdField, *args: Any, **kwargs: Any) -> None:
        self.path += country_id
        super().__init__(client, *args, **kwargs)
