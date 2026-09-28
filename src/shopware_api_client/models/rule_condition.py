from typing import Annotated, Any

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class RuleConditionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "rule_condition"

    type: str
    rule_id: Annotated[IdField, RefersTo("rule")]
    script_id: Annotated[IdField | None, RefersTo("app_script_condition")] = None
    parent_id: Annotated[IdField | None, RefersTo("rule_condition")] = None
    value: Any | None = None
    position: int | None = None
