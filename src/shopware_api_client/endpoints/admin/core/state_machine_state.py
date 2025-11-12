from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.state_machine_state import StateMachineState as StateMachineStateBase


class StateMachineState(StateMachineStateBase, AdminModel["StateMachineStateEndpoint"]):
    state_machine_id: IdField
    state_machine: ForeignRelation["StateMachine"]
    from_state_machine_transitions: ManyRelation["StateMachineTransition"]
    to_state_machine_transitions: ManyRelation["StateMachineTransition"]
    order_transactions: ManyRelation["OrderTransaction"]
    order_deliveries: ManyRelation["OrderDelivery"]
    orders: ManyRelation["Order"]
    order_transaction_captures: ManyRelation["OrderTransactionCapture"]
    order_transaction_capture_refunds: ManyRelation["OrderTransactionCaptureRefund"]
    to_state_machine_history_entries: ManyRelation["StateMachineHistory"]
    from_state_machine_history_entries: ManyRelation["StateMachineHistory"]


class StateMachineStateEndpoint(AdminEndpoint[StateMachineState]):
    name = "state_machine_state"
    path = "/state-machine-state"
    model_class = StateMachineState


from .order import Order  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .order_transaction import OrderTransaction  # noqa: E402
from .order_transaction_capture import OrderTransactionCapture  # noqa: E402
from .order_transaction_capture_refund import OrderTransactionCaptureRefund  # noqa: E402
from .state_machine import StateMachine  # noqa: E402
from .state_machine_history import StateMachineHistory  # noqa: E402
from .state_machine_transition import StateMachineTransition  # noqa: E402
