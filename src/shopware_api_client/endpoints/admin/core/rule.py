from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.rule import RuleBase


class Rule(RuleBase, AdminModel["RuleEndpoint"]):
    product_prices: ManyRelation["ProductPrice"] = Field(default=...)
    shipping_methods: ManyRelation["ShippingMethod"] = Field(default=...)
    payment_methods: ManyRelation["PaymentMethod"] = Field(default=...)
    persona_promotions: ManyRelation["Promotion"] = Field(default=...)
    tags: ManyRelation["Tag"] = Field(default=...)
    order_promotions: ManyRelation["Promotion"] = Field(default=...)
    cart_promotions: ManyRelation["Promotion"] = Field(default=...)
    promotion_discounts: ManyRelation["PromotionDiscount"] = Field(default=...)
    conditions: ManyRelation["RuleCondition"] = Field(default=...)

    """
    Todo:
    shipping_method_prices[ShippingMethodPrice],
    shipping_method_price_calculations[ShippingMethodPrice], flow_sequences[FlowSequence], tax_providers[TaxProvider],
    promotion_set_groups[PromotionSetGroup]
    """


class RuleEndpoint(AdminEndpoint[Rule]):
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
