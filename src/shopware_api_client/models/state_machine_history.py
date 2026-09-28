
from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class StateMachineHistoryBase(ApiModelBase):
    _identifier: str = "state_machine_history"

    state_machine_id: Annotated[IdField, RefersTo("state_machine")]
    entity_name: str
    from_state_id: Annotated[IdField, RefersTo("state_machine_state")]
    to_state_id: Annotated[IdField, RefersTo("state_machine_state")]
    transition_action_name: str | None = None
    user_id: Annotated[IdField | None, RefersTo("user")] = None
    entity_id: IdField | None = None
    referenced_id: IdField | None = None
    referenced_version_id: IdField | None = None
