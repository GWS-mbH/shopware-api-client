from pydantic import AwareDatetime

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Data, IdField
from ...relations import ForeignRelation


class TaxRuleBase(ApiModelBase[EndpointClass]):
    _identifier: str = "tax_rule"

    tax_rule_type_id: IdField
    country_id: IdField
    tax_rate: float
    data: Data | None = None
    tax_id: IdField
    active_from: AwareDatetime | None = None


class TaxRuleRelations:
    tax_rule_type: ForeignRelation["TaxRuleType"]
    country: ForeignRelation["Country"]
    tax: ForeignRelation["Tax"]


class TaxRule(TaxRuleBase["TaxRuleEndpoint"], TaxRuleRelations):
    pass


class TaxRuleEndpoint(EndpointBase[TaxRule]):
    name = "tax_rule"
    path = "/tax-rule"
    model_class = TaxRule


from .country import Country  # noqa: E402
from .tax import Tax  # noqa: E402
from .tax_rule_type import TaxRuleType  # noqa: E402
