from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.order_delivery import OrderDeliveryBase


class OrderDelivery(OrderDeliveryBase, AdminModel["OrderDeliveryEndpoint"]):
    state: ForeignRelation["StateMachineState"] = Field(default=...)
    order: ForeignRelation["Order"] = Field(default=...)
    shipping_order_address: ForeignRelation["OrderAddress"] = Field(default=...)
    shipping_method: ForeignRelation["ShippingMethod"] = Field(default=...)
    positions: ManyRelation["OrderDeliveryPosition"] = Field(default=...)


class OrderDeliveryEndpoint(AdminEndpoint[OrderDelivery]):
    name = "order_delivery"
    path = "/order-delivery"
    model_class = OrderDelivery


from .order import Order  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from .order_delivery_position import OrderDeliveryPosition  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
