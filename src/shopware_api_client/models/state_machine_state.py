from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class StateMachineStateBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "state_machine_state"

    technical_name: str
    name: str
