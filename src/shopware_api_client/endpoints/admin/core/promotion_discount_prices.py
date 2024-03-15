from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class PromotionDiscountPricesBase(ApiModelBase[EndpointClass]):
    _identifier: str = "promotion_discount_prices"

    discount_id: IdField
    currency_id: IdField
    price: float


class PromotionDiscountPricesRelations:
    discount: ForeignRelation["PromotionDiscount"]
    currency: ForeignRelation["Currency"]


class PromotionDiscountPrices(
    PromotionDiscountPricesBase["PromotionDiscountPricesEndpoint"], PromotionDiscountPricesRelations
):
    pass


class PromotionDiscountPricesEndpoint(EndpointBase[PromotionDiscountPrices]):
    name = "promotion_discount_prices"
    path = "/promotion-discount-prices"
    model_class = PromotionDiscountPrices


from .currency import Currency  # noqa: E402
from .promotion_discount import PromotionDiscount  # noqa: E402
