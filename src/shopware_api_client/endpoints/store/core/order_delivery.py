from shopware_api_client.models.order_delivery import OrderDeliveryBase


class OrderDelivery(OrderDeliveryBase):
    state_machine_stateL: "StateMachineState | None" = None
    shipping_order_address: "OrderAddress | None" = None
    shipping_method: "ShippingMethod | None" = None
    positions: list["OrderDeliveryPosition"] | None = None


from .order_address import OrderAddress  # noqa: E402
from .order_delivery_position import OrderDeliveryPosition  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
