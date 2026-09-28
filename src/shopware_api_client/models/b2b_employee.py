from typing import Annotated

from pydantic import AwareDatetime

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class B2bEmployeeBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "b2b_employee"

    business_partner_customer_id: Annotated[IdField | None, RefersTo("customer")] = None
    role_id: Annotated[IdField | None, RefersTo("b2b_components_role")] = None
    language_id: Annotated[IdField, RefersTo("language")]
    active: bool | None = None
    first_name: str
    last_name: str
    email: str
    recovery_time: AwareDatetime | None = None
