from shopware_api_client.base import StoreSearchEndpoint, EndpointMixin
from shopware_api_client.models.currency import Currency as CurrencyBase


class Currency(CurrencyBase, EndpointMixin["CurrencyEndpoint"]):
    pass


class CurrencyEndpoint(StoreSearchEndpoint[Currency]):
    model_class = Currency
    name = "currency"
    path = "/currency"
