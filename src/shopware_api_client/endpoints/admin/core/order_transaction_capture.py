from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.order_transaction_capture import OrderTransactionCaptureBase


class OrderTransactionCapture(OrderTransactionCaptureBase, AdminModel["OrderTransactionCaptureEndpoint"]):
    state: ForeignRelation["StateMachineState"]
    order_transaction: ForeignRelation["OrderTransaction"]
    refunds: ManyRelation["OrderTransactionCaptureRefund"]


class OrderTransactionCaptureEndpoint(AdminEndpoint[OrderTransactionCapture]):
    name = "order_transaction_capture"
    path = "/order-transaction-capture"
    model_class = OrderTransactionCapture


from .order_transaction import OrderTransaction  # noqa: E402
from .order_transaction_capture_refund import OrderTransactionCaptureRefund  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
