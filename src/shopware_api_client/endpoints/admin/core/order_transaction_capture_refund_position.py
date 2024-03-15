from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation


class OrderTransactionCaptureRefundPositionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_transaction_capture_refund_position"

    version_id: IdField | None = None
    refund_id: IdField
    refund_version_id: IdField | None = None
    order_line_item_id: IdField
    order_line_item_version_id: IdField | None = None
    external_reference: str | None = None
    reason: str | None = None
    quantity: int | None = None
    amount: Amount
    custom_fields: dict[str, Any] | None = None


class OrderTransactionCaptureRefundPositionRelations:
    order_line_item: ForeignRelation["OrderLineItem"]
    refund: ForeignRelation["OrderTransactionCaptureRefund"]


class OrderTransactionCaptureRefundPosition(
    OrderTransactionCaptureRefundPositionBase["OrderTransactionCaptureRefundPositionEndpoint"],
    OrderTransactionCaptureRefundPositionRelations,
):
    pass


class OrderTransactionCaptureRefundPositionEndpoint(EndpointBase[OrderTransactionCaptureRefundPosition]):
    name = "order_transaction_capture_refund_position"
    path = "/order-transaction-capture-refund-position"
    model_class = OrderTransactionCaptureRefundPosition


from .order_line_item import OrderLineItem  # noqa: E402
from .order_transaction_capture_refund import OrderTransactionCaptureRefund  # noqa: E402
