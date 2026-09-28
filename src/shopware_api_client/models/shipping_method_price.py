from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.price import Price


class ShippingMethodPriceBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "shipping_method_price"

    shipping_method_id: Annotated[IdField, RefersTo("shipping_method")]
    rule_id: Annotated[IdField | None, RefersTo("rule")]
    calculation: int | None = None
    calculation_rule_id: Annotated[IdField | None, RefersTo("rule")]
    quantity_start: float | None = None
    quantity_end: float | None = None
    currency_price: list[Price] | None = None
