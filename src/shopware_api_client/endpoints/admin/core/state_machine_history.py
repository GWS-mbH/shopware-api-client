from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class StateMachineHistoryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "state_machine_history"

    state_machine_id: IdField
    entity_name: str
    from_state_id: IdField
    to_state_id: IdField
    transition_action_name: str | None = None
    user_id: IdField | None = None
    entity_id: dict[str, Any]
    referenced_id: IdField | None = None
    referenced_version_id: IdField | None = None


class StateMachineHistoryRelations:
    state_machine: ForeignRelation["StateMachine"]
    from_state: ForeignRelation["StateMachineState"]
    to_state: ForeignRelation["StateMachineState"]
    user: ForeignRelation["User"]


class StateMachineHistory(StateMachineHistoryBase["StateMachineHistoryEndpoint"], StateMachineHistoryRelations):
    pass


class StateMachineHistoryEndpoint(EndpointBase[StateMachineHistory]):
    name = "state_machine_history"
    path = "/state-machine-history"
    model_class = StateMachineHistory


from .state_machine import StateMachine  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
from .user import User  # noqa: E402
