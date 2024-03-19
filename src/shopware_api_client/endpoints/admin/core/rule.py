from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class RuleBase(ApiModelBase[EndpointClass]):
    _identifier: str = "rule"

    name: str
    priority: int
    description: str | None = None
    invalid: bool | None = Field(default=None, exclude=True)
    areas: list[str] | None = Field(default=None, exclude=True)
    custom_fields: dict[str, Any] | None = None
    module_types: dict[str, Any] | None = None


class RuleRelations:
    product_prices: ManyRelation["ProductPrice"]
    shipping_methods: ManyRelation["ShippingMethod"]
    payment_methods: ManyRelation["PaymentMethod"]
    persona_promotions: ManyRelation["Promotion"]
    tags: ManyRelation["Tag"]
    order_promotions: ManyRelation["Promotion"]
    cart_promotions: ManyRelation["Promotion"]
    promotion_discounts: ManyRelation["PromotionDiscount"]
    conditions: ManyRelation["RuleCondition"]

    """
    Todo:
    shipping_method_prices[ShippingMethodPrice],
    shipping_method_price_calculations[ShippingMethodPrice], flow_sequences[FlowSequence], tax_providers[TaxProvider],
    promotion_set_groups[PromotionSetGroup]
    """


class Rule(RuleBase["RuleEndpoint"], RuleRelations):
    pass


class RuleEndpoint(EndpointBase[Rule]):
    name = "rule"
    path = "/rule"
    model_class = Rule


from .payment_method import PaymentMethod  # noqa: E402
from .product_price import ProductPrice  # noqa: E402
from .promotion import Promotion  # noqa: E402
from .promotion_discount import PromotionDiscount  # noqa: E402
from .rule_condition import RuleCondition  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
from .tag import Tag  # noqa: E402
