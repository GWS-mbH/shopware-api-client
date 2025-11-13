from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.promotion_discount import PromotionDiscountBase


class PromotionDiscount(PromotionDiscountBase, AdminModel["PromotionDiscountEndpoint"]):
    promotion: ForeignRelation["Promotion"]
    discount_rules: ManyRelation["Rule"]
    promotion_discount_prices: ManyRelation["PromotionDiscountPrices"]


class PromotionDiscountEndpoint(AdminEndpoint[PromotionDiscount]):
    name = "promotion_discount"
    path = "/promotion-discount"
    model_class = PromotionDiscount


from .promotion import Promotion  # noqa: E402
from .promotion_discount_prices import PromotionDiscountPrices  # noqa: E402
from .rule import Rule  # noqa: E402
