from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import Data, IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Country, Tax, TaxRuleType


class TaxRuleBase(ApiModelBase[EndpointClass]):
    _identifier: str = "tax_rule"

    tax_rule_type_id: IdField = Field(
        ..., serialization_alias="taxRuleTypeId", validation_alias=AliasChoices("tax_rule_type_id", "taxRuleTypeId")
    )
    country_id: IdField = Field(
        ..., serialization_alias="countryId", validation_alias=AliasChoices("country_id", "countryId")
    )
    tax_rate: float = Field(..., serialization_alias="taxRate", validation_alias=AliasChoices("tax_rate", "taxRate"))
    data: Data | None = None
    tax_id: IdField = Field(..., serialization_alias="taxId", validation_alias=AliasChoices("tax_id", "taxId"))
    active_from: AwareDatetime | None = Field(
        default=None, serialization_alias="activeFrom", validation_alias=AliasChoices("active_from", "activeFrom")
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class TaxRuleRelations:
    tax_rule_type: ClassVar[ForeignRelation["TaxRuleType"]] = ForeignRelation("TaxRuleType", "tax_rule_type_id")
    country: ClassVar[ForeignRelation["Country"]] = ForeignRelation("Country", "country_id")
    tax: ClassVar[ForeignRelation["Tax"]] = ForeignRelation("Tax", "tax_id")


class TaxRule(TaxRuleBase["TaxRuleEndpoint"], TaxRuleRelations):
    pass


class TaxRuleEndpoint(EndpointBase[TaxRule]):
    name = "tax_rule"
    path = "/tax-rule"
    model_class = TaxRule


registry.register_admin(TaxRuleEndpoint)
