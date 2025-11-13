from typing import Any

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class RuleConditionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "rule_condition"

    type: str
    rule_id: IdField
    script_id: IdField | None = None
    parent_id: IdField | None = None
    value: Any | None = None
    position: int | None = None
