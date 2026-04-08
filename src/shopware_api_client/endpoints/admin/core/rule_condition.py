from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.rule_condition import RuleConditionBase


class RuleCondition(RuleConditionBase, AdminModel["RuleConditionEndpoint"]):
    rule: ForeignRelation["Rule"] = Field(default=...)
    app_script_condition: ForeignRelation["AppScriptCondition"] = Field(default=...)
    parent: ForeignRelation["RuleCondition"] = Field(default=...)
    children: ManyRelation["RuleCondition"] = Field(default=...)


class RuleConditionEndpoint(AdminEndpoint[RuleCondition]):
    name = "rule_condition"
    path = "/rule-condition"
    model_class = RuleCondition


from .app_script_condition import AppScriptCondition  # noqa: E402
from .rule import Rule  # noqa: E402
