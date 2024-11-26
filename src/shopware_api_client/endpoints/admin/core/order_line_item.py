from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation


class OrderLineItemBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_line_item"

    version_id: IdField | None = None
    order_id: IdField
    order_version_id: IdField | None = None
    product_id: IdField | None = None
    product_version_id: IdField | None = None
    promotion_id: IdField | None = Field(default=None, exclude=True)
    parent_id: IdField | None = None
    parent_version_id: IdField | None = None
    cover_id: IdField | None = None
    identifier: str
    referenced_id: str | None = None
    quantity: int
    label: str
    payload: dict[str, Any] | list | None = None
    good: bool | None = None
    removable: bool | None = None
    stackable: bool | None = None
    position: int
    states: list[str]
    price: Amount
    price_definition: dict[str, Any] | None = None
    unit_price: float | None = None
    total_price: float | None = None
    description: str | None = None
    type: str | None = None
    custom_fields: dict[str, Any] | None = None


class OrderLineItemRelations:
    cover: ForeignRelation["Media"]
    order: ForeignRelation["Order"]
    product: ForeignRelation["Product"]
    promotion: ForeignRelation["Promotion"]
    order_delivery_positions: ManyRelation["OrderDeliveryPosition"]
    order_transaction_capture_refund_positions: ManyRelation["OrderTransactionCaptureRefundPosition"]
    downloads: ManyRelation["OrderLineItemDownload"]
    parent: ForeignRelation["OrderLineItem"]
    children: ManyRelation["OrderLineItem"]


class OrderLineItem(OrderLineItemBase["OrderLineItemEndpoint"], OrderLineItemRelations):
    pass


class OrderLineItemEndpoint(EndpointBase[OrderLineItem]):
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
