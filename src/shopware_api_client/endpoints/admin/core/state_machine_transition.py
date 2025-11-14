from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.state_machine_transition import StateMachineTransitionBase


class StateMachineTransition(StateMachineTransitionBase, AdminModel["StateMachineTransitionEndpoint"]):
    state_machine: ForeignRelation["StateMachine"]
    from_state: ForeignRelation["StateMachineState"]
    to_state: ForeignRelation["StateMachineState"]


class StateMachineTransitionEndpoint(AdminEndpoint[StateMachineTransition]):
    name = "state_machine_transition"
    path = "/state-machine-transition"
    model_class = StateMachineTransition


from .state_machine import StateMachine  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
