from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.tax_rule_type import TaxRuleType as TaxRuleTypeBase


class TaxRuleType(TaxRuleTypeBase, AdminModel["TaxRuleTypeEndpoint"]):
    rules: ManyRelation["TaxRule"]


class TaxRuleTypeEndpoint(AdminEndpoint[TaxRuleType]):
    name = "tax_rule_type"
    path = "/tax-rule-type"
    model_class = TaxRuleType


from .tax_rule import TaxRule  # noqa: E402
