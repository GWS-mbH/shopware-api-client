from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.order_delivery_position import OrderDeliveryPositionBase


class OrderDeliveryPosition(OrderDeliveryPositionBase, AdminModel["OrderDeliveryPositionEndpoint"]):
    order_delivery: ForeignRelation["OrderDelivery"] = Field(default=...)
    order_line_item: ForeignRelation["OrderLineItem"] = Field(default=...)


class OrderDeliveryPositionEndpoint(AdminEndpoint[OrderDeliveryPosition]):
    name = "order_delivery_position"
    path = "/order-delivery-position"
    model_class = OrderDeliveryPosition


from .order_delivery import OrderDelivery  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
