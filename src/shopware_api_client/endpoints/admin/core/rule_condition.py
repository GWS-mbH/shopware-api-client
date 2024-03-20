from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class RuleConditionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "rule_condition"

    type: str
    rule_id: IdField
    script_id: IdField | None = None
    parent_id: IdField | None = None
    value: Any | None = None
    position: int | None = None
    custom_fields: dict[str, Any] | None = None


class RuleConditionRelations:
    rule: ForeignRelation["Rule"]
    app_script_condition: ForeignRelation["AppScriptCondition"]
    parent: ForeignRelation["RuleCondition"]
    children: ManyRelation["RuleCondition"]


class RuleCondition(RuleConditionBase["RuleConditionEndpoint"], RuleConditionRelations):
    pass


class RuleConditionEndpoint(EndpointBase[RuleCondition]):
    name = "rule_condition"
    path = "/rule-condition"
    model_class = RuleCondition


from .app_script_condition import AppScriptCondition  # noqa: E402
from .rule import Rule  # noqa: E402
