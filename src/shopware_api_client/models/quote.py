from typing import Annotated

from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.calculated_price import CalculatedPrice
from shopware_api_client.structs.cart_price import CartPrice


class QuoteBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote"

    auto_increment: int | None = Field(default=None, exclude=True)
    quote_number: str | None = None
    user_id: Annotated[IdField | None, RefersTo("user")] = None
    currency_id: Annotated[IdField, RefersTo("currency")]
    language_id: Annotated[IdField, RefersTo("language")]
    sales_channel_id: Annotated[IdField, RefersTo("sales_channel")]
    customer_id: Annotated[IdField, RefersTo("customer")]
    created_by_id: Annotated[IdField | None, RefersTo("user")] = None
    updated_by_id: Annotated[IdField | None, RefersTo("user")] = None
    order_id: Annotated[IdField | None, RefersTo("order")] = None
    order_version_id: IdField | None = None
    expiration_date: AwareDatetime | None = None
    sent_at: AwareDatetime | None = None
    price: CartPrice | None = None
    shipping_costs: CalculatedPrice | None = None
    discount: float | None = None
    tax_status: str | None = Field(default=None, exclude=True)
    amount_total: float | None = Field(default=None, exclude=True)
    amount_net: float | None = Field(default=None, exclude=True)
    subtotal_net: float | None = None
    total_discount: float | None = None
    cart_payload: str | None = None
