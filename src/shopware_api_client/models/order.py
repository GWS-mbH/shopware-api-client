from datetime import date
from typing import Annotated

from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.calculated_price import CalculatedPrice
from shopware_api_client.structs.cart_price import CartPrice


class OrderBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order"

    auto_increment: int | None = Field(default=None, exclude=True)
    order_number: str | None = None
    billing_address_id: Annotated[IdField, RefersTo("order_address")]
    billing_address_version_id: IdField | None = None
    currency_id: Annotated[IdField, RefersTo("currency")]
    language_id: Annotated[IdField, RefersTo("language")]
    sales_channel_id: Annotated[IdField, RefersTo("sales_channel")]
    order_date_time: AwareDatetime
    order_date: date | None = Field(default=None, exclude=True)
    price: CartPrice | None = None
    amount_total: float | None = Field(default=None, exclude=True)
    amount_net: float | None = Field(default=None, exclude=True)
    position_price: float | None = Field(default=None, exclude=True)
    tax_status: str | None = Field(default=None, exclude=True)
    shipping_costs: CalculatedPrice | None = None
    shipping_total: float | None = Field(default=None, exclude=True)
    currency_factor: float
    deep_link_code: str | None = None
    affiliate_code: str | None = None
    campaign_code: str | None = None
    customer_comment: str | None = None
    source: str | None = None
    rule_ids: list[str] | None = None
    created_by_id: Annotated[IdField | None, RefersTo("user")] = None
    updated_by_id: Annotated[IdField | None, RefersTo("user")] = None
