from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class PromotionDiscountPricesBase(ApiModelBase):
    _identifier: str = "promotion_discount_prices"

    discount_id: Annotated[IdField, RefersTo("promotion_discount")]
    currency_id: Annotated[IdField, RefersTo("currency")]
    price: float
