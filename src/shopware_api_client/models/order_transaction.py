from typing import Annotated

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.calculated_price import CalculatedPrice


class OrderTransactionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_transaction"

    order_id: Annotated[IdField, RefersTo("order")]
    order_version_id: IdField | None = None
    payment_method_id: Annotated[IdField, RefersTo("payment_method")]
    amount: CalculatedPrice
    state_id: Annotated[IdField, RefersTo("state_machine_state")] = Field(..., exclude=True)
