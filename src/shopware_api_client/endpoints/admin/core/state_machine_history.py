from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.state_machine_history import StateMachineHistoryBase


class StateMachineHistory(StateMachineHistoryBase, AdminModel["StateMachineHistoryEndpoint"]):
    state_machine: ForeignRelation["StateMachine"] = Field(default=...)
    from_state: ForeignRelation["StateMachineState"] = Field(default=...)
    to_state: ForeignRelation["StateMachineState"] = Field(default=...)
    user: ForeignRelation["User"] = Field(default=...)


class StateMachineHistoryEndpoint(AdminEndpoint[StateMachineHistory]):
    name = "state_machine_history"
    path = "/state-machine-history"
    model_class = StateMachineHistory


from .state_machine import StateMachine  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
from .user import User  # noqa: E402
