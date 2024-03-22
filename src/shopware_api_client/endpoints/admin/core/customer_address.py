from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class CustomerAddressBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer_address"

    customer_id: IdField
    country_id: IdField
    country_state_id: IdField | None = None
    salutation_id: IdField | None = None
    first_name: str
    last_name: str
    zipcode: str | None = None
    city: str
    company: str | None = None
    street: str
    department: str | None = None
    title: str | None = None
    phone_number: str | None = None
    additional_address_line1: str | None = None
    additional_address_line2: str | None = None
    custom_fields: dict[str, Any] | None = None


class CustomerAddressRelations:
    customer: ForeignRelation["Customer"]
    country: ForeignRelation["Country"]
    country_state: ForeignRelation["CountryState"]
    salutation: ForeignRelation["Salutation"]


class CustomerAddress(CustomerAddressBase["CustomerAddressEndpoint"], CustomerAddressRelations):
    pass


class CustomerAddressEndpoint(EndpointBase[CustomerAddress]):
    name = "customer_address"
    path = "/customer-address"
    model_class = CustomerAddress


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .customer import Customer  # noqa: E402
from .salutation import Salutation  # noqa: E402
