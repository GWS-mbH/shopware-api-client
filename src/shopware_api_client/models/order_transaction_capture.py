from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import Amount, IdField


class OrderTransactionCapture(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_transaction_capture"

    version_id: IdField | None = None
    order_transaction_id: IdField
    order_transaction_version_id: IdField | None = None
    state_id: IdField = Field(..., exclude=True)
    external_reference: str | None = None
    amount: Amount
