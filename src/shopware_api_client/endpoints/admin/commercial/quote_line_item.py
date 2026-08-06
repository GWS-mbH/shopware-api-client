from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.quote_line_item import QuoteLineItemBase


class QuoteLineItem(QuoteLineItemBase, AdminModel["QuoteLineItemEndpoint"]):
    quote: ForeignRelation["Quote"] = Field(default=...)
    parent: ForeignRelation["QuoteLineItem"] = Field(default=...)
    children: ManyRelation["QuoteLineItem"] = Field(default=...)
    product: ForeignRelation["Product"] = Field(default=...)
    promotion: ForeignRelation["Promotion"] = Field(default=...)
    cover: ForeignRelation["Media"] = Field(default=...)
    delivery_positions: ManyRelation["QuoteDeliveryPosition"] = Field(default=...)


class QuoteLineItemEndpoint(AdminEndpoint[QuoteLineItem]):
    name = "quote_line_item"
    path = "/quote-line-item"
    model_class = QuoteLineItem


from ..core.media import Media  # noqa: E402
from ..core.product import Product  # noqa: E402
from ..core.promotion import Promotion  # noqa: E402
from .quote_delivery_position import QuoteDeliveryPosition  # noqa: E402
from .quote import Quote  # noqa: E402
