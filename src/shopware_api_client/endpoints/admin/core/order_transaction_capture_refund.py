from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation


class OrderTransactionCaptureRefundBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_transaction_capture_refund"

    version_id: IdField | None = None
    capture_id: IdField
    capture_version_id: IdField | None = None
    state_id: IdField = Field(..., exclude=True)
    external_reference: str | None = None
    reason: str | None = None
    amount: Amount
    custom_fields: dict[str, Any] | None = None


class OrderTransactionCaptureRefundRelations:
    state: ForeignRelation["StateMachineState"]
    capture: ForeignRelation["OrderTransactionCapture"]
    positions: ManyRelation["OrderTransactionCaptureRefundPosition"]


class OrderTransactionCaptureRefund(
    OrderTransactionCaptureRefundBase["OrderTransactionCaptureRefundEndpoint"], OrderTransactionCaptureRefundRelations
):
    pass


class OrderTransactionCaptureRefundEndpoint(EndpointBase[OrderTransactionCaptureRefund]):
    name = "order_transaction_capture_refund"
    path = "/order-transaction-capture-refund"
    model_class = OrderTransactionCaptureRefund


from .order_transaction_capture import OrderTransactionCapture  # noqa: E402
from .order_transaction_capture_refund_position import OrderTransactionCaptureRefundPosition  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
