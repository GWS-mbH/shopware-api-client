from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, Price


class ShippingMethodPrice(ApiModelBase, CustomFieldsMixin):
    _identifier = "shipping_method_price"

    shipping_method_id: IdField
    rule_id: IdField | None
    calculation: int | None = None
    calculation_rule_id: IdField | None
    quantity_start: float | None = None
    quantity_end: float | None = None
    currency_price: list[Price] | None = None
