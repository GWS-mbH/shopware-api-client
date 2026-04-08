from shopware_api_client.models.order_transaction_capture_refund import OrderTransactionCaptureRefundBase


class OrderTransactionCaptureRefund(OrderTransactionCaptureRefundBase):
    state_machine_state: "StateMachineState | None" = None
    transaction_capture: "OrderTransactionCapture | None" = None
    positions: list["OrderTransactionCaptureRefundPosition"] | None = None


from .order_transaction_capture import OrderTransactionCapture  # noqa: E402
from .order_transaction_capture_refund_position import OrderTransactionCaptureRefundPosition  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
