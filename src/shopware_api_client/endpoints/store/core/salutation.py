from shopware_api_client.base import StoreSearchEndpoint, EndpointMixin
from shopware_api_client.models.salutation import SalutationBase


class Salutation(SalutationBase, EndpointMixin["SalutationEndpoint"]):
    pass


class SalutationEndpoint(StoreSearchEndpoint[Salutation]):
    model_class = Salutation
    name = "salutation"
    path = "/salutation"
