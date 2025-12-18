from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.promotion_discount_prices import PromotionDiscountPricesBase


class PromotionDiscountPrices(PromotionDiscountPricesBase, AdminModel["PromotionDiscountPricesEndpoint"]):
    discount: ForeignRelation["PromotionDiscount"] = Field(default=...)
    currency: ForeignRelation["Currency"] = Field(default=...)


class PromotionDiscountPricesEndpoint(AdminEndpoint[PromotionDiscountPrices]):
    name = "promotion_discount_prices"
    path = "/promotion-discount-prices"
    model_class = PromotionDiscountPrices


from .currency import Currency  # noqa: E402
from .promotion_discount import PromotionDiscount  # noqa: E402
