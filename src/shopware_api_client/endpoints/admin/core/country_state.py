from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.country_state import CountryStateBase


class CountryState(CountryStateBase, AdminModel["CountryStateEndpoint"]):
    country: ForeignRelation["Country"] = Field(default=...)
    customer_addresses: ManyRelation["CustomerAddress"] = Field(default=...)
    order_addresses: ManyRelation["OrderAddress"] = Field(default=...)


class CountryStateEndpoint(AdminEndpoint[CountryState]):
    name = "country_state"
    path = "/country_state"
    model_class = CountryState


from .country import Country  # noqa: E402
from .customer_address import CustomerAddress  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
