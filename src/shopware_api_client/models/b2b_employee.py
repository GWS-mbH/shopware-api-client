from pydantic import AwareDatetime

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class B2bEmployeeBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "b2b_employee"

    business_partner_customer_id: IdField | None = None
    role_id: IdField | None = None
    language_id: IdField
    active: bool | None = None
    first_name: str
    last_name: str
    email: str
    recovery_time: AwareDatetime | None = None
