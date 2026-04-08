
from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class StateMachineHistoryBase(ApiModelBase):
    _identifier: str = "state_machine_history"

    state_machine_id: IdField
    entity_name: str
    from_state_id: IdField
    to_state_id: IdField
    transition_action_name: str | None = None
    user_id: IdField | None = None
    entity_id: IdField | None = None
    referenced_id: IdField | None = None
    referenced_version_id: IdField | None = None
