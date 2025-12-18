from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.customer_address import CustomerAddressBase


class CustomerAddress(CustomerAddressBase, AdminModel["CustomerAddressEndpoint"]):
    country: ForeignRelation["Country"] = Field(default=...)
    country_state: ForeignRelation["CountryState"] = Field(default=...)
    salutation: ForeignRelation["Salutation"] = Field(default=...)
    customer: ForeignRelation["Customer"] = Field(default=...)


class CustomerAddressEndpoint(AdminEndpoint[CustomerAddress]):
    name = "customer_address"
    path = "/customer-address"
    model_class = CustomerAddress


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .customer import Customer  # noqa: E402
from .salutation import Salutation  # noqa: E402
