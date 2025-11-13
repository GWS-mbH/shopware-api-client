from shopware_api_client.models.order_transaction import OrderTransactionBase


class OrderTransaction(OrderTransactionBase):
    state_machine_state: "StateMachineState | None" = None
    payment_method: "PaymentMethod | None" = None
    captures: list["OrderTransactionCapture"] | None = None


from .order_transaction_capture import OrderTransactionCapture  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
