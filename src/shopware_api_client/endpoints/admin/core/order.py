from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.order import OrderBase
from shopware_api_client.structs.cash_rounding_config import CashRoundingConfig


class Order(OrderBase, AdminModel["OrderEndpoint"]):
    state_id: IdField = Field(..., exclude=True)
    item_rounding: CashRoundingConfig
    total_rounding: CashRoundingConfig
    order_customer: "OrderCustomer"
    state: ForeignRelation["StateMachineState"] = Field(default=...)
    currency: ForeignRelation["Currency"] = Field(default=...)
    language: ForeignRelation["Language"] = Field(default=...)
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    addresses: ManyRelation["OrderAddress"] = Field(default=...)
    billing_address: ForeignRelation["OrderAddress"] = Field(default=...)
    deliveries: ManyRelation["OrderDelivery"] = Field(default=...)
    line_items: ManyRelation["OrderLineItem"] = Field(default=...)
    transactions: ManyRelation["OrderTransaction"] = Field(default=...)
    documents: ManyRelation["Document"] = Field(default=...)
    tags: ManyRelation["Tag"] = Field(default=...)
    created_by: ForeignRelation["User"] = Field(default=...)
    updated_by: ForeignRelation["User"] = Field(default=...)


class OrderEndpoint(AdminEndpoint[Order]):
    name = "order"
    path = "/order"
    model_class = Order


from .currency import Currency  # noqa: E402
from .document import Document  # noqa: E402
from .language import Language  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from shopware_api_client.endpoints.admin.core.order_customer import OrderCustomer  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
from .order_transaction import OrderTransaction  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
from .tag import Tag  # noqa: E402
from .user import User  # noqa: E402
