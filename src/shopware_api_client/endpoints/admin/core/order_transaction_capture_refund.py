from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.order_transaction_capture_refund import OrderTransactionCaptureRefundBase


class OrderTransactionCaptureRefund(
    OrderTransactionCaptureRefundBase, AdminModel["OrderTransactionCaptureRefundEndpoint"]
):
    state: ForeignRelation["StateMachineState"] = Field(default=...)
    capture: ForeignRelation["OrderTransactionCapture"] = Field(default=...)
    positions: ManyRelation["OrderTransactionCaptureRefundPosition"] = Field(default=...)


class OrderTransactionCaptureRefundEndpoint(AdminEndpoint[OrderTransactionCaptureRefund]):
    name = "order_transaction_capture_refund"
    path = "/order-transaction-capture-refund"
    model_class = OrderTransactionCaptureRefund


from .order_transaction_capture import OrderTransactionCapture  # noqa: E402
from .order_transaction_capture_refund_position import OrderTransactionCaptureRefundPosition  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
