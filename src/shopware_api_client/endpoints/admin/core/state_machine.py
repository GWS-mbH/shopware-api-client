from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.state_machine import StateMachineBase


class StateMachine(StateMachineBase, AdminModel["StateMachineEndpoint"]):
    states: ManyRelation["StateMachineState"] = Field(default=...)
    transitions: ManyRelation["StateMachineTransition"] = Field(default=...)
    history_entries: ManyRelation["StateMachineHistory"] = Field(default=...)


class StateMachineEndpoint(AdminEndpoint[StateMachine]):
    name = "state_machine"
    path = "/state-machine"
    model_class = StateMachine


from .state_machine_history import StateMachineHistory  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
from .state_machine_transition import StateMachineTransition  # noqa: E402
