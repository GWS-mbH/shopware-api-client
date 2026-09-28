from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class CustomerAddressBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "customer_address"

    customer_id: Annotated[IdField, RefersTo("customer")]
    country_id: Annotated[IdField, RefersTo("country")]
    country_state_id: Annotated[IdField | None, RefersTo("country_state")] = None
    salutation_id: Annotated[IdField | None, RefersTo("salutation")] = None
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
