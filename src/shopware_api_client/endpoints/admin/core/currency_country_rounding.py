from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField, Rounding
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Country, Currency


class CurrencyCountryRoundingBase(ApiModelBase[EndpointClass]):
    _identifier: str = "currency_country_rounding"

    currency_id: IdField = Field(
        ..., serialization_alias="currencyId", validation_alias=AliasChoices("currency_id", "currencyId")
    )
    country_id: IdField = Field(
        ..., serialization_alias="countryId", validation_alias=AliasChoices("country_id", "countryId")
    )
    item_rounding: Rounding = Field(
        ..., serialization_alias="itemRounding", validation_alias=AliasChoices("item_rounding", "itemRounding")
    )
    total_rounding: Rounding = Field(
        ..., serialization_alias="totalRounding", validation_alias=AliasChoices("total_rounding", "totalRounding")
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


class CurrencyCountryRoundingRelations:
    currency: ClassVar[ForeignRelation["Currency"]] = ForeignRelation("Currency", "currency_id")
    country: ClassVar[ForeignRelation["Country"]] = ForeignRelation("Country", "country_id")


class CurrencyCountryRounding(
    CurrencyCountryRoundingBase["CurrencyCountryRoundingEndpoint"], CurrencyCountryRoundingRelations
):
    pass


class CurrencyCountryRoundingEndpoint(EndpointBase[CurrencyCountryRounding]):
    name = "currency_country_rounding"
    path = "/currency-country-rounding"
    model_class = CurrencyCountryRounding


registry.register_admin(CurrencyCountryRoundingEndpoint)
