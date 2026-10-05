from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class StateMachineTransitionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "state_machine_transition"

    action_name: str
    state_machine_id: Annotated[IdField, RefersTo("state_machine")]
    from_state_id: Annotated[IdField, RefersTo("state_machine_state")]
    to_state_id: Annotated[IdField, RefersTo("state_machine_state")]
