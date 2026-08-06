from datetime import date

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.calculated_price import CalculatedPrice
from shopware_api_client.structs.cart_price import CartPrice


class QuoteBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote"

    auto_increment: int | None = Field(default=None, exclude=True)
    quote_number: str | None = None
    user_id: IdField
    currency_id: IdField
    language_id: IdField
    sales_channel_id: IdField
    default_billing_address_id: IdField
    customer_id: IdField
    created_by_id: IdField | None = None
    updated_by_id: IdField | None = None
    order_id: IdField | None = None
    order_version_id: IdField | None = None
    expiration_date: date | None = None # TODO
    sent_at: date | None = None
    price: CartPrice | None = None
    shipping_costs: CalculatedPrice | None = None
    discount: float | None = None
    tax_status: str | None = Field(default=None, exclude=True)
    amount_total: float | None = Field(default=None, exclude=True)
    amount_net: float | None = Field(default=None, exclude=True)
    subtotal_net: float | None = None
    total_discount: float | None = None
    cart_payload: str | None = None
    created_at: date
    updated_at: date | None
