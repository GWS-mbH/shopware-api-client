from shopware_api_client.base import StoreSearchEndpoint, EndpointMixin
from shopware_api_client.models.country import CountryBase


class Country(CountryBase, EndpointMixin["CountryEndpoint"]):
    states: list["CountryState"] | None = None


class CountryEndpoint(StoreSearchEndpoint[Country]):
    model_class = Country
    name = "country"
    path = "/country"


from .country_state import CountryState  # noqa: E402
