from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.quote import QuoteBase
from shopware_api_client.structs.cash_rounding_config import CashRoundingConfig


class Quote(QuoteBase, AdminModel["QuoteEndpoint"]):
    state_id: IdField = Field(..., exclude=True)
    user: ForeignRelation["User"] = Field(default=...)
    currency: ForeignRelation["Currency"] = Field(default=...)
    language: ForeignRelation["Language"] = Field(default=...)
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    customer: ForeignRelation["Customer"] = Field(default=...)
    order: ForeignRelation["Order"] = Field(default=...)
    item_rounding: CashRoundingConfig
    total_rounding: CashRoundingConfig
    state: ForeignRelation["StateMachineState"] = Field(default=...)
    created_by: ForeignRelation["User"] = Field(default=...)
    updated_by: ForeignRelation["User"] = Field(default=...)
    line_items: ManyRelation["QuoteLineItem"] = Field(default=...)
    deliveries: ManyRelation["QuoteDelivery"] = Field(default=...)
    transactions: ManyRelation["QuoteTransaction"] = Field(default=...)
    comments: ManyRelation["QuoteComment"] = Field(default=...)
    quote_employees: ManyRelation["QuoteEmployee"] = Field(default=...)
    documents: ManyRelation["QuoteDocument"] = Field(default=...)



class QuoteEndpoint(AdminEndpoint[Quote]):
    name = "quote"
    path = "/quote"
    model_class = Quote

from ..core.currency import Currency  # noqa: E402
from ..core.customer import Customer  # noqa: E402
from ..core.language import Language  # noqa: E402
from ..core.order import Order  # noqa: E402
from ..core.sales_channel import SalesChannel  # noqa: E402
from ..core.state_machine_state import StateMachineState  # noqa: E402
from ..core.user import User  # noqa: E402
from .quote_comment import QuoteComment  # noqa: E402
from .quote_delivery import QuoteDelivery  # noqa: E402
from .quote_document import QuoteDocument  # noqa: E402
from .quote_employee import QuoteEmployee  # noqa: E402
from .quote_line_item import QuoteLineItem  # noqa: E402
from .quote_transaction import QuoteTransaction  # noqa: E402
