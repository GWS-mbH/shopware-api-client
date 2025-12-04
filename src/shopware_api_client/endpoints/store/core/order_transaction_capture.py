from shopware_api_client.models.order_transaction_capture import OrderTransactionCaptureBase


class OrderTransactionCapture(OrderTransactionCaptureBase):
    state_machine_state: "StateMachineState | None" = None
    transaction: "OrderTransaction | None" = None
    refunds: list["OrderTransactionCaptureRefund"] | None = None


from .order_transaction import OrderTransaction  # noqa: E402
from .order_transaction_capture_refund import OrderTransactionCaptureRefund  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
