from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import Rounding
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import (
        CurrencyCountryRounding,
        Order,
        ProductExport,
        PromotionDiscountPrices,
        SalesChannel,
        SalesChannelDomain,
    )


class CurrencyBase(ApiModelBase[EndpointClass]):
    _identifier: str = "currency"

    factor: float
    symbol: str
    iso_code: str = Field(..., serialization_alias="isoCode", validation_alias=AliasChoices("iso_code", "isoCode"))
    short_name: str = Field(
        ..., serialization_alias="shortName", validation_alias=AliasChoices("short_name", "shortName")
    )
    name: str
    position: int | None = None
    is_system_default: bool | None = Field(
        None,
        alias="isSystemDefault",
        description="Runtime field, cannot be used as part of the criteria.",
    )
    tax_free_from: float | None = Field(
        default=None, serialization_alias="taxFreeFrom", validation_alias=AliasChoices("tax_free_from", "taxFreeFrom")
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
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
    translated: dict[str, Any] | None = None


class CurrencyRelations:
    sales_channel_default_assignments: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "salesChannelDefaultAssignments"
    )
    orders: ClassVar[ManyRelation["Order"]] = ManyRelation("Order", "orders")
    sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "salesChannels")
    sales_channel_domains: ClassVar[ManyRelation["SalesChannelDomain"]] = ManyRelation(
        "SalesChannelDomain", "salesChannelDomains"
    )
    promotion_discount_prices: ClassVar[ManyRelation["PromotionDiscountPrices"]] = ManyRelation(
        "PromotionDiscountPrices", "promotionDiscountPrices"
    )
    product_exports: ClassVar[ManyRelation["ProductExport"]] = ManyRelation("ProductExport", "productExports")
    country_roundings: ClassVar[ManyRelation["CurrencyCountryRounding"]] = ManyRelation(
        "CurrencyCountryRounding", "countryRoundings"
    )


class Currency(CurrencyBase["CurrencyEndpoint"], CurrencyRelations):
    pass


class CurrencyEndpoint(EndpointBase[Currency]):
    name = "currency"
    path = "/currency"
    model_class = Currency


registry.register_admin(CurrencyEndpoint)
