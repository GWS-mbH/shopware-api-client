from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class QuoteCommentBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_comment"

    comment: str
    seen_at: AwareDatetime | None = None
    quote_id: IdField
    quote_version_id: IdField | None = None
    state_id: IdField | None = Field(default=None, exclude=True)
    customer_id: IdField | None = None
    employee_id: IdField | None = None
    created_by_id: IdField | None = None
