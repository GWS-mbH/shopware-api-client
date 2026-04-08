from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.calculated_price import CalculatedPrice


class OrderTransactionCaptureRefundPositionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_transaction_capture_refund_position"

    refund_id: IdField
    refund_version_id: IdField | None = None
    order_line_item_id: IdField
    order_line_item_version_id: IdField | None = None
    external_reference: str | None = None
    reason: str | None = None
    quantity: int | None = None
    amount: CalculatedPrice
