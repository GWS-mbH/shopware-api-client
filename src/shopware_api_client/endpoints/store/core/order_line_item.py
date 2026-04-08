from shopware_api_client.models.order_line_item import OrderLineItemBase


class OrderLineItem(OrderLineItemBase):
    cover: "Media | None" = None
    product: "Product | None" = None
    order_delivery_positions: list["OrderDeliveryPosition"] | None = None
    parent: "OrderLineItem | None" = None
    children: list["OrderLineItem"] | None = None


from .media import Media  # noqa: E402
from .order_delivery_position import OrderDeliveryPosition  # noqa: E402
from .product import Product  # noqa: E402
