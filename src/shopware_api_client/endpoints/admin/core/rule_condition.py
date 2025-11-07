from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.rule_condition import RuleCondition as RuleConditionBase


class RuleCondition(RuleConditionBase, AdminModel["RuleConditionEndpoint"]):
    rule: ForeignRelation["Rule"]
    app_script_condition: ForeignRelation["AppScriptCondition"]
    parent: ForeignRelation["RuleCondition"]
    children: ManyRelation["RuleCondition"]


class RuleConditionEndpoint(AdminEndpoint[RuleCondition]):
    name = "rule_condition"
    path = "/rule-condition"
    model_class = RuleCondition


from .app_script_condition import AppScriptCondition  # noqa: E402
from .rule import Rule  # noqa: E402
