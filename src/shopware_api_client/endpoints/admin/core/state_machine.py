from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ManyRelation


class StateMachineBase(ApiModelBase[EndpointClass]):
    _identifier: str = "state_machine"

    technical_name: str
    name: str
    custom_fields: dict[str, Any] | None = None
    initial_state_id: IdField | None = None
    translated: dict[str, Any] | None = None


class StateMachineRelations:
    states: ManyRelation["StateMachineState"]
    transitions: ManyRelation["StateMachineTransition"]
    history_entries: ManyRelation["StateMachineHistory"]


class StateMachine(StateMachineBase["StateMachineEndpoint"], StateMachineRelations):
    pass


class StateMachineEndpoint(EndpointBase[StateMachine]):
    name = "state_machine"
    path = "/state-machine"
    model_class = StateMachine


from .state_machine_history import StateMachineHistory  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
from .state_machine_transition import StateMachineTransition  # noqa: E402
