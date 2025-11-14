from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class StateMachineTransitionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "state_machine_transition"

    action_name: str
    state_machine_id: IdField
    from_state_id: IdField
    to_state_id: IdField
