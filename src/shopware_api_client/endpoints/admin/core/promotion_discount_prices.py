from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Currency, PromotionDiscount


class PromotionDiscountPricesBase(ApiModelBase[EndpointClass]):
    _identifier: str = "promotion_discount_prices"

    discount_id: IdField = Field(
        ..., serialization_alias="discountId", validation_alias=AliasChoices("discount_id", "discountId")
    )
    currency_id: IdField = Field(
        ..., serialization_alias="currencyId", validation_alias=AliasChoices("currency_id", "currencyId")
    )
    price: float
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class PromotionDiscountPricesRelations:
    discount: ClassVar[ForeignRelation["PromotionDiscount"]] = ForeignRelation("PromotionDiscount", "discount_id")
    currency: ClassVar[ForeignRelation["Currency"]] = ForeignRelation("Currency", "currency_id")


class PromotionDiscountPrices(
    PromotionDiscountPricesBase["PromotionDiscountPricesEndpoint"], PromotionDiscountPricesRelations
):
    pass


class PromotionDiscountPricesEndpoint(EndpointBase[PromotionDiscountPrices]):
    name = "promotion_discount_prices"
    path = "/promotion-discount-prices"
    model_class = PromotionDiscountPrices


registry.register_admin(PromotionDiscountPricesEndpoint)
