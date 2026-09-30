from typing import Annotated

from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class QuoteCommentBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_comment"

    comment: str
    seen_at: AwareDatetime | None = None
    quote_id: Annotated[IdField, RefersTo("quote")]
    quote_version_id: IdField | None = None
    state_id: Annotated[IdField | None, RefersTo("state_machine_state")] = Field(default=None, exclude=True)
    customer_id: Annotated[IdField | None, RefersTo("customer")] = None
    employee_id: Annotated[IdField | None, RefersTo("b2b_employee")] = None
    created_by_id: Annotated[IdField | None, RefersTo("user")] = None
