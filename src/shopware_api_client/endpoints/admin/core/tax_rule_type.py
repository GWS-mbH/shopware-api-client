from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import TaxRule


class TaxRuleTypeBase(ApiModelBase[EndpointClass]):
    _identifier: str = "tax_rule_type"

    technical_name: str = Field(
        ...,
        serialization_alias="technicalName",
        validation_alias=AliasChoices("technical_name", "technicalName"),
        exclude=True,
    )
    position: int
    type_name: str = Field(..., serialization_alias="typeName", validation_alias=AliasChoices("type_name", "typeName"))
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )
    translated: dict[str, Any] | None = None


class TaxRuleTypeRelations:
    rules: ClassVar[ManyRelation["TaxRule"]] = ManyRelation("TaxRule", "rules")


class TaxRuleType(TaxRuleTypeBase["TaxRuleTypeEndpoint"], TaxRuleTypeRelations):
    pass


class TaxRuleTypeEndpoint(EndpointBase[TaxRuleType]):
    name = "tax_rule_type"
    path = "/tax-rule-type"
    model_class = TaxRuleType


registry.register_admin(TaxRuleTypeEndpoint)
