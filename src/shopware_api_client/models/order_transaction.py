from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.calculated_price import CalculatedPrice


class OrderTransactionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_transaction"

    order_id: IdField
    order_version_id: IdField | None = None
    payment_method_id: IdField
    amount: CalculatedPrice
    state_id: IdField = Field(..., exclude=True)
