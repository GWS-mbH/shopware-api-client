from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class StateMachineState(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "state_machine_state"

    technical_name: str
    name: str
    state_machine_id: IdField
