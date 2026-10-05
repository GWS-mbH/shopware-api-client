from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.calculated_price import CalculatedPrice


class QuoteDeliveryPositionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_delivery_position"

    quote_delivery_id: Annotated[IdField, RefersTo("quote_delivery")]
    quote_delivery_version_id: IdField | None = None
    quote_line_item_id: Annotated[IdField, RefersTo("quote_line_item")]
    quote_line_item_version_id: IdField | None = None
    price: CalculatedPrice | None = None
    unit_price: float | None = None
    total_price: float | None = None
    quantity: int | None = None
