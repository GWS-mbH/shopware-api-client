from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Promotion, PromotionDiscountPrices, Rule


class PromotionDiscountBase(ApiModelBase[EndpointClass]):
    _identifier: str = "promotion_discount"

    promotion_id: IdField = Field(
        ..., serialization_alias="promotionId", validation_alias=AliasChoices("promotion_id", "promotionId")
    )
    scope: str
    type: str
    value: float
    consider_advanced_rules: bool = Field(
        ...,
        serialization_alias="considerAdvancedRules",
        validation_alias=AliasChoices("consider_advanced_rules", "considerAdvancedRules"),
    )
    max_value: float | None = Field(
        default=None, serialization_alias="maxValue", validation_alias=AliasChoices("max_value", "maxValue")
    )
    sorter_key: str | None = Field(
        default=None, serialization_alias="sorterKey", validation_alias=AliasChoices("sorter_key", "sorterKey")
    )
    applier_key: str | None = Field(
        default=None, serialization_alias="applierKey", validation_alias=AliasChoices("applier_key", "applierKey")
    )
    usage_key: str | None = Field(
        default=None, serialization_alias="usageKey", validation_alias=AliasChoices("usage_key", "usageKey")
    )
    picker_key: str | None = Field(
        default=None, serialization_alias="pickerKey", validation_alias=AliasChoices("picker_key", "pickerKey")
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


class PromotionDiscountRelations:
    promotion: ClassVar[ForeignRelation["Promotion"]] = ForeignRelation("Promotion", "promotion_id")
    discount_rules: ClassVar[ManyRelation["Rule"]] = ManyRelation("Rule", "discountRules")
    promotion_discount_prices: ClassVar[ManyRelation["PromotionDiscountPrices"]] = ManyRelation(
        "PromotionDiscountPrices", "promotion-discount-prices"
    )


class PromotionDiscount(PromotionDiscountBase["PromotionDiscountEndpoint"], PromotionDiscountRelations):
    pass


class PromotionDiscountEndpoint(EndpointBase[PromotionDiscount]):
    name = "promotion_discount"
    path = "/promotion-discount"
    model_class = PromotionDiscount


registry.register_admin(PromotionDiscountEndpoint)
