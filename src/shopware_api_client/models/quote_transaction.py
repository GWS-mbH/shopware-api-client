from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.calculated_price import CalculatedPrice


class QuoteTransactionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_transaction"

    quote_id: Annotated[IdField, RefersTo("quote")]
    quote_version_id: IdField | None = None
    payment_method_id: Annotated[IdField, RefersTo("payment_method")]
    amount: CalculatedPrice
