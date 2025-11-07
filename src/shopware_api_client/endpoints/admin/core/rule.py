from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.rule import Rule as RuleBase


class Rule(RuleBase, AdminModel["RuleEndpoint"]):
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
