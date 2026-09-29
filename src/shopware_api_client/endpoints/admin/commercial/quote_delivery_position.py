from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.quote_delivery_position import QuoteDeliveryPositionBase


class QuoteDeliveryPosition(QuoteDeliveryPositionBase, AdminModel["QuoteDeliveryPositionEndpoint"]):
    quote_delivery: ForeignRelation["QuoteDelivery"] = Field(default=...)
    quote_line_item: ForeignRelation["QuoteLineItem"] = Field(default=...)


class QuoteDeliveryPositionEndpoint(AdminEndpoint[QuoteDeliveryPosition]):
    name = "quote_delivery_position"
    path = "/quote-delivery-position"
    model_class = QuoteDeliveryPosition


from .quote_delivery import QuoteDelivery  # noqa: E402
from .quote_line_item import QuoteLineItem  # noqa: E402
