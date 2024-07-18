from typing import Any

from pydantic import AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Amount, IdField, Price, Rounding
from ...relations import ForeignRelation, ManyRelation


class OrderBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order"

    version_id: IdField | None = None
    auto_increment: int | None = Field(default=None, exclude=True)
    order_number: str | None = None
    billing_address_id: IdField
    billing_address_version_id: IdField | None = None
    currency_id: IdField
    language_id: IdField
    sales_channel_id: IdField
    order_date_time: AwareDatetime
    order_date: str | None = Field(default=None, exclude=True)
    price: Price | None = None
    amount_total: float | None = Field(default=None, exclude=True)
    amount_net: float | None = Field(default=None, exclude=True)
    position_price: float | None = Field(default=None, exclude=True)
    tax_status: str | None = Field(default=None, exclude=True)
    shipping_costs: Amount | None = None
    shipping_total: float | None = Field(default=None, exclude=True)
    order_customer: "OrderCustomer"
    currency_factor: float
    deep_link_code: str | None = None
    affiliate_code: str | None = None
    campaign_code: str | None = None
    customer_comment: str | None = None
    source: str | None = None
    state_id: IdField = Field(..., exclude=True)
    rule_ids: list[str] | None = None
    custom_fields: dict[str, Any] | None = None
    created_by_id: IdField | None = None
    updated_by_id: IdField | None = None
    item_rounding: Rounding
    total_rounding: Rounding


class OrderRelations:
    state: ForeignRelation["StateMachineState"]
    currency: ForeignRelation["Currency"]
    language: ForeignRelation["Language"]
    sales_channel: ForeignRelation["SalesChannel"]
    addresses: ManyRelation["OrderAddress"]
    billing_address: ForeignRelation["OrderAddress"]
    deliveries: ManyRelation["OrderDelivery"]
    line_items: ManyRelation["OrderLineItem"]
    transactions: ManyRelation["OrderTransaction"]
    documents: ManyRelation["Document"]
    tags: ManyRelation["Tag"]
    created_by: ForeignRelation["User"]
    updated_by: ForeignRelation["User"]


class Order(OrderBase["OrderEndpoint"], OrderRelations):
    pass


class OrderEndpoint(EndpointBase[Order]):
    name = "order"
    path = "/order"
    model_class = Order


from .currency import Currency  # noqa: E402
from .document import Document  # noqa: E402
from .language import Language  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from .order_customer import OrderCustomer  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
from .order_transaction import OrderTransaction  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
from .tag import Tag  # noqa: E402
from .user import User  # noqa: E402
