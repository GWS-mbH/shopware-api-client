from shopware_api_client.models.order_transaction_capture_refund_position import \
    OrderTransactionCaptureRefundPositionBase


class OrderTransactionCaptureRefundPosition(OrderTransactionCaptureRefundPositionBase):
    order_line_item: "OrderLineItem | None" = None
    order_transaction_capture_refund: "OrderTransactionCaptureRefund | None" = None


from .order_line_item import OrderLineItem  # noqa: E402
from .order_transaction_capture_refund import OrderTransactionCaptureRefund  # noqa: E402
