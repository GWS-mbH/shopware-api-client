from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.order_line_item import OrderLineItemBase
from shopware_api_client.structs.calculated_price import CalculatedPrice


class OrderLineItem(OrderLineItemBase, AdminModel["OrderLineItemEndpoint"]):
    price: CalculatedPrice
    cover: ForeignRelation["Media"] = Field(default=...)
    order: ForeignRelation["Order"] = Field(default=...)
    product: ForeignRelation["Product"] = Field(default=...)
    promotion: ForeignRelation["Promotion"] = Field(default=...)
    order_delivery_positions: ManyRelation["OrderDeliveryPosition"] = Field(default=...)
    order_transaction_capture_refund_positions: ManyRelation["OrderTransactionCaptureRefundPosition"] = Field(default=...)
    downloads: ManyRelation["OrderLineItemDownload"] = Field(default=...)
    parent: ForeignRelation["OrderLineItem"] = Field(default=...)
    children: ManyRelation["OrderLineItem"] = Field(default=...)


class OrderLineItemEndpoint(AdminEndpoint[OrderLineItem]):
    name = "order_line_item"
    path = "/order-line-item"
    model_class = OrderLineItem


from .media import Media  # noqa: E402
from .order import Order  # noqa: E402
from .order_delivery_position import OrderDeliveryPosition  # noqa: E402
from .order_line_item_download import OrderLineItemDownload  # noqa: E402
from .order_transaction_capture_refund_position import OrderTransactionCaptureRefundPosition  # noqa: E402
from .product import Product  # noqa: E402
from .promotion import Promotion  # noqa: E402
