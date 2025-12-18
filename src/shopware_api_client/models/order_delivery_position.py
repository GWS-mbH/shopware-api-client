from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.calculated_price import CalculatedPrice


class OrderDeliveryPositionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_delivery_position"

    order_delivery_id: IdField
    order_delivery_version_id: IdField | None = None
    order_line_item_id: IdField
    order_line_item_version_id: IdField | None = None
    price: CalculatedPrice | None = None
    unit_price: float | None = None
    total_price: float | None = None
    quantity: int | None = None
