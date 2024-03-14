from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import PaymentMethod, ProductPrice, Promotion, PromotionDiscount, ShippingMethod, Tag


class RuleBase(ApiModelBase[EndpointClass]):
    _identifier: str = "rule"

    name: str
    priority: int
    description: str | None = None
    invalid: bool | None = Field(default=None, exclude=True)
    areas: list[str] | None = Field(default=None, exclude=True)
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    module_types: dict[str, Any] | None = Field(
        default=None, serialization_alias="moduleTypes", validation_alias=AliasChoices("module_types", "moduleTypes")
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


class RuleRelations:
    product_prices: ClassVar[ManyRelation["ProductPrice"]] = ManyRelation("ProductPrice", "productPrices")
    shipping_methods: ClassVar[ManyRelation["ShippingMethod"]] = ManyRelation("ShippingMethod", "shippingMethods")
    payment_methods: ClassVar[ManyRelation["PaymentMethod"]] = ManyRelation("PaymentMethod", "paymentMethods")
    persona_promotions: ClassVar[ManyRelation["Promotion"]] = ManyRelation("Promotion", "personaPromotions")
    tags: ClassVar[ManyRelation["Tag"]] = ManyRelation("Tag", "tags")
    order_promotions: ClassVar[ManyRelation["Promotion"]] = ManyRelation("Promotion", "orderPromotions")
    cart_promotions: ClassVar[ManyRelation["Promotion"]] = ManyRelation("Promotion", "cartPromotions")
    promotion_discounts: ClassVar[ManyRelation["PromotionDiscount"]] = ManyRelation(
        "PromotionDiscount", "promotionDiscounts"
    )

    """
    Todo:
    conditions[RuleCondition], shipping_method_prices[ShippingMethodPrice],
    shipping_method_price_calculations[ShippingMethodPrice], flow_sequences[FlowSequence], tax_providers[TaxProvider],
    promotion_set_groups[PromotionSetGroup]
    """


class Rule(RuleBase["RuleEndpoint"], RuleRelations):
    pass


class RuleEndpoint(EndpointBase[Rule]):
    name = "rule"
    path = "/rule"
    model_class = Rule


registry.register_admin(RuleEndpoint)
