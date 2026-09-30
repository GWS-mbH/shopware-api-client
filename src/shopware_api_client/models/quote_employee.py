from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class QuoteEmployeeBase(ApiModelBase):
    _identifier: str = "quote_employee"

    quote_id: IdField
    quote_version_id: IdField | None = None
    employee_id: IdField
    first_name: str
    last_name: str
