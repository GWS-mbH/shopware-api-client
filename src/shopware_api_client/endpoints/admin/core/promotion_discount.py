from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class PromotionDiscountBase(ApiModelBase[EndpointClass]):
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


class PromotionDiscountRelations:
    promotion: ForeignRelation["Promotion"]
    discount_rules: ManyRelation["Rule"]
    promotion_discount_prices: ManyRelation["PromotionDiscountPrices"]


class PromotionDiscount(PromotionDiscountBase["PromotionDiscountEndpoint"], PromotionDiscountRelations):
    pass


class PromotionDiscountEndpoint(EndpointBase[PromotionDiscount]):
    name = "promotion_discount"
    path = "/promotion-discount"
    model_class = PromotionDiscount


from .promotion import Promotion  # noqa: E402
from .promotion_discount_prices import PromotionDiscountPrices  # noqa: E402
from .rule import Rule  # noqa: E402
