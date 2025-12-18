from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.calculated_price import CalculatedPrice


class OrderTransactionCaptureRefundBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_transaction_capture_refund"

    capture_id: IdField
    capture_version_id: IdField | None = None
    state_id: IdField = Field(..., exclude=True)
    external_reference: str | None = None
    reason: str | None = None
    amount: CalculatedPrice
