from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import Amount, IdField


class OrderTransactionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_transaction"

    version_id: IdField | None = None
    order_id: IdField
    order_version_id: IdField | None = None
    payment_method_id: IdField
    amount: Amount
    state_id: IdField = Field(..., exclude=True)
