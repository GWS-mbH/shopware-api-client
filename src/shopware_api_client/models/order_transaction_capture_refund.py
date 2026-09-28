from typing import Annotated

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.calculated_price import CalculatedPrice


class OrderTransactionCaptureRefundBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_transaction_capture_refund"

    capture_id: Annotated[IdField, RefersTo("order_transaction_capture")]
    capture_version_id: IdField | None = None
    state_id: Annotated[IdField, RefersTo("state_machine_state")] = Field(..., exclude=True)
    external_reference: str | None = None
    reason: str | None = None
    amount: CalculatedPrice
