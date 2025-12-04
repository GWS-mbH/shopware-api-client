from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class PromotionDiscountPricesBase(ApiModelBase):
    _identifier: str = "promotion_discount_prices"

    discount_id: IdField
    currency_id: IdField
    price: float
