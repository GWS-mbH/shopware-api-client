from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation


class OrderTransactionCaptureBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_transaction_capture"

    version_id: IdField | None = None
    order_transaction_id: IdField
    order_transaction_version_id: IdField | None = None
    state_id: IdField = Field(..., exclude=True)
    external_reference: str | None = None
    amount: Amount
    custom_fields: dict[str, Any] | None = None


class OrderTransactionCaptureRelations:
    state: ForeignRelation["StateMachineState"]
    order_transaction: ForeignRelation["OrderTransaction"]
    refunds: ManyRelation["OrderTransactionCaptureRefund"]


class OrderTransactionCapture(
    OrderTransactionCaptureBase["OrderTransactionCaptureEndpoint"], OrderTransactionCaptureRelations
):
    pass


class OrderTransactionCaptureEndpoint(EndpointBase[OrderTransactionCapture]):
    name = "order_transaction_capture"
    path = "/order-transaction-capture"
    model_class = OrderTransactionCapture


from .order_transaction import OrderTransaction  # noqa: E402
from .order_transaction_capture_refund import OrderTransactionCaptureRefund  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
