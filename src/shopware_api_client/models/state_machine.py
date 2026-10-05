from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class StateMachineBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "state_machine"

    technical_name: str
    name: str
    initial_state_id: Annotated[IdField | None, RefersTo("state_machine_state")] = None
