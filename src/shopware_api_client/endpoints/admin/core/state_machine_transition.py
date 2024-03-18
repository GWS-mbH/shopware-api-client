from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class StateMachineTransitionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "state_machine_transition"

    action_name: str
    state_machine_id: IdField
    from_state_id: IdField
    to_state_id: IdField
    custom_fields: dict[str, Any] | None = None


class StateMachineTransitionRelations:
    state_machine: ForeignRelation["StateMachine"]
    from_state: ForeignRelation["StateMachineState"]
    to_state: ForeignRelation["StateMachineState"]


class StateMachineTransition(
    StateMachineTransitionBase["StateMachineTransitionEndpoint"], StateMachineTransitionRelations
):
    pass


class StateMachineTransitionEndpoint(EndpointBase[StateMachineTransition]):
    name = "state_machine_transition"
    path = "/state-machine-transition"
    model_class = StateMachineTransition


from .state_machine import StateMachine  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
