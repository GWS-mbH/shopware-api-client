from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.quote_delivery import QuoteDeliveryBase


class QuoteDelivery(QuoteDeliveryBase, AdminModel["QuoteDeliveryEndpoint"]):
    quote: ForeignRelation["Quote"] = Field(default=...)
    shipping_method: ForeignRelation["ShippingMethod"] = Field(default=...)
    positions: ManyRelation["QuoteDeliveryPosition"] = Field(default=...)


class QuoteDeliveryEndpoint(AdminEndpoint[QuoteDelivery]):
    name = "quote_delivery"
    path = "/quote-delivery"
    model_class = QuoteDelivery


from ..core.shipping_method import ShippingMethod  # noqa: E402
from .quote import Quote  # noqa: E402
from .quote_delivery_position import QuoteDeliveryPosition  # noqa: E402
