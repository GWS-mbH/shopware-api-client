from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.shipping_method import ShippingMethodBase


class ShippingMethod(ShippingMethodBase, AdminModel["ShippingMethodEndpoint"]):
    delivery_time: ForeignRelation["DeliveryTime"] = Field(default=...)
    availability_rule: ForeignRelation["Rule"] = Field(default=...)
    prices: ManyRelation["ShippingMethodPrice"] = Field(default=...)
    media: ForeignRelation["Media"] = Field(default=...)
    tags: ManyRelation["Tag"] = Field(default=...)
    order_deliveries: ManyRelation["OrderDelivery"] = Field(default=...)
    sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    sales_channel_default_assignments: ManyRelation["SalesChannel"] = Field(default=...)
    tax: ForeignRelation["Tax"] = Field(default=...)

    """
    Todo:
    app_shipping_method[AppShippingMethod]
    """


class ShippingMethodEndpoint(AdminEndpoint[ShippingMethod]):
    name = "shipping_method"
    path = "/shipping-method"
    model_class = ShippingMethod


from .delivery_time import DeliveryTime  # noqa: E402
from .media import Media  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .rule import Rule  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .shipping_method_price import ShippingMethodPrice  # noqa: E402
from .tag import Tag  # noqa: E402
from .tax import Tax  # noqa: E402
