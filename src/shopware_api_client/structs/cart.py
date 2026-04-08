from typing import Any

from pydantic import Field

from .cart_price import CartPrice
from .delivery import Delivery
from .line_item import LineItem
from .transaction import Transaction
from ..fieldsets import FieldSetBase


class Cart(FieldSetBase):
    name: str | None = None
    token: str | None = None
    price: CartPrice
    line_items: list[LineItem]
    errors: list[dict[str, Any]] | dict[str, Any] | None = Field(default=None)
    deliveries: list[Delivery] | None = None
    transactions: list[Transaction] | None = None
    modified: bool | None = False
    customer_comment: str | None = None
    affiliate_code: str | None = None
    campaign_code: str | None = None
