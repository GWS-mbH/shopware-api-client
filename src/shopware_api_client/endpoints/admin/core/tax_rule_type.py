from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class TaxRuleTypeBase(ApiModelBase[EndpointClass]):
    _identifier: str = "tax_rule_type"

    technical_name: str = Field(default="", exclude=True)
    position: int
    type_name: str
    translated: dict[str, Any] | None = None


class TaxRuleTypeRelations:
    rules: ManyRelation["TaxRule"]


class TaxRuleType(TaxRuleTypeBase["TaxRuleTypeEndpoint"], TaxRuleTypeRelations):
    pass


class TaxRuleTypeEndpoint(EndpointBase[TaxRuleType]):
    name = "tax_rule_type"
    path = "/tax-rule-type"
    model_class = TaxRuleType


from .tax_rule import TaxRule  # noqa: E402
