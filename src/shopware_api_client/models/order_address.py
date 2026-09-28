from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class OrderAddressBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_address"

    country_id: Annotated[IdField, RefersTo("country")]
    country_state_id: Annotated[IdField | None, RefersTo("country_state")] = None
    order_version_id: IdField | None = None
    salutation_id: Annotated[IdField | None, RefersTo("salutation")] = None
    first_name: str
    last_name: str
    street: str
    zipcode: str | None = None
    city: str
    company: str | None = None
    department: str | None = None
    title: str | None = None
    vat_id: str | None = None
    phone_number: str | None = None
    additional_address_line1: str | None = None
    additional_address_line2: str | None = None
