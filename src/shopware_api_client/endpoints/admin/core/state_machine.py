from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.state_machine import StateMachine as StateMachineBase


class StateMachine(StateMachineBase, AdminModel["StateMachineEndpoint"]):
    states: ManyRelation["StateMachineState"]
    transitions: ManyRelation["StateMachineTransition"]
    history_entries: ManyRelation["StateMachineHistory"]


class StateMachineEndpoint(AdminEndpoint[StateMachine]):
    name = "state_machine"
    path = "/state-machine"
    model_class = StateMachine


from .state_machine_history import StateMachineHistory  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
from .state_machine_transition import StateMachineTransition  # noqa: E402
