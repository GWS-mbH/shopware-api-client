from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class QuoteEmployeeBase(ApiModelBase):
    _identifier: str = "quote_employee"

    quote_id: Annotated[IdField, RefersTo("quote")]
    quote_version_id: IdField | None = None
    employee_id: Annotated[IdField, RefersTo("b2b_employee")]
    first_name: str
    last_name: str
