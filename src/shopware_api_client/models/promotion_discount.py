from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class PromotionDiscountBase(ApiModelBase):
    _identifier: str = "promotion_discount"

    promotion_id: IdField
    scope: str
    type: str
    value: float
    consider_advanced_rules: bool
    max_value: float | None = None
    sorter_key: str | None = None
    applier_key: str | None = None
    usage_key: str | None = None
    picker_key: str | None = None
