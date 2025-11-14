from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.tax_rule import TaxRuleBase


class TaxRule(TaxRuleBase, AdminModel["TaxRuleEndpoint"]):
    tax_rule_type: ForeignRelation["TaxRuleType"]
    country: ForeignRelation["Country"]
    tax: ForeignRelation["Tax"]


class TaxRuleEndpoint(AdminEndpoint[TaxRule]):
    name = "tax_rule"
    path = "/tax-rule"
    model_class = TaxRule


from .country import Country  # noqa: E402
from .tax import Tax  # noqa: E402
from .tax_rule_type import TaxRuleType  # noqa: E402
