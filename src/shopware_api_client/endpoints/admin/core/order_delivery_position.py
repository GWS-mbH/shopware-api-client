from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField, Price
from ...relations import ForeignRelation


class OrderDeliveryPositionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_delivery_position"

    version_id: IdField | None = None
    order_delivery_id: IdField
    order_delivery_version_id: IdField | None = None
    order_line_item_id: IdField
    order_line_item_version_id: IdField | None = None
    price: Price | None = None
    unit_price: float | None = None
    total_price: float | None = None
    quantity: int | None = None
    custom_fields: dict[str, Any] | None = None


class OrderDeliveryPositionRelations:
    order_delivery: ForeignRelation["OrderDelivery"]
    order_line_item: ForeignRelation["OrderLineItem"]


class OrderDeliveryPosition(OrderDeliveryPositionBase["OrderDeliveryPositionEndpoint"], OrderDeliveryPositionRelations):
    pass


class OrderDeliveryPositionEndpoint(EndpointBase[OrderDeliveryPosition]):
    name = "order_delivery_position"
    path = "/order-delivery-position"
    model_class = OrderDeliveryPosition


from .order_delivery import OrderDelivery  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
