from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.calculated_price import CalculatedPrice


class QuoteDeliveryPositionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_delivery_position"

    quote_delivery_id: IdField
    quote_delivery_version_id: IdField | None = None
    quote_line_item_id: IdField
    quote_line_item_version_id: IdField | None = None
    price: CalculatedPrice | None = None
    unit_price: float | None = None
    total_price: float | None = None
    quantity: int | None = None
