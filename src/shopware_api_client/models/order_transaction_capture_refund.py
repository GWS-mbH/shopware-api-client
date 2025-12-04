from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import Amount, IdField


class OrderTransactionCaptureRefundBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_transaction_capture_refund"

    version_id: IdField | None = None
    capture_id: IdField
    capture_version_id: IdField | None = None
    state_id: IdField = Field(..., exclude=True)
    external_reference: str | None = None
    reason: str | None = None
    amount: Amount
