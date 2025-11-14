from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.app_script_condition import AppScriptConditionBase


class AppScriptCondition(AppScriptConditionBase, AdminModel["AppScriptConditionEndpoint"]):
    app: ForeignRelation["App"]
    rule_conditions: ManyRelation["RuleCondition"]


class AppScriptConditionEndpoint(AdminEndpoint[AppScriptCondition]):
    name = "app_script_condition"
    path = "/app-script-condition"
    model_class = AppScriptCondition


from .app import App  # noqa: E402
from .rule_condition import RuleCondition  # noqa: E402
