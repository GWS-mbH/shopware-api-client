from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.order_transaction_capture_refund_position import (
    OrderTransactionCaptureRefundPosition as OrderTransactionCaptureRefundPositionBase,
)


class OrderTransactionCaptureRefundPosition(
    OrderTransactionCaptureRefundPositionBase, AdminModel["OrderTransactionCaptureRefundPositionEndpoint"]
):
    order_line_item: ForeignRelation["OrderLineItem"]
    refund: ForeignRelation["OrderTransactionCaptureRefund"]


class OrderTransactionCaptureRefundPositionEndpoint(AdminEndpoint[OrderTransactionCaptureRefundPosition]):
    name = "order_transaction_capture_refund_position"
    path = "/order-transaction-capture-refund-position"
    model_class = OrderTransactionCaptureRefundPosition


from .order_line_item import OrderLineItem  # noqa: E402
from .order_transaction_capture_refund import OrderTransactionCaptureRefund  # noqa: E402
