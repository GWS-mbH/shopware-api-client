from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.models.customer_address import CustomerAddressBase
from shopware_api_client.endpoints.relations import ForeignRelation


class CustomerAddress(CustomerAddressBase, AdminModel["CustomerAddressEndpoint"]):
    country: ForeignRelation["Country"]
    country_state: ForeignRelation["CountryState"]
    salutation: ForeignRelation["Salutation"]
    customer: ForeignRelation["Customer"]


class CustomerAddressEndpoint(AdminEndpoint[CustomerAddress]):
    name = "customer_address"
    path = "/customer-address"
    model_class = CustomerAddress


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .customer import Customer  # noqa: E402
from .salutation import Salutation  # noqa: E402
