from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class ShippingMethodBase(ApiModelBase[EndpointClass]):
    _identifier: str = "shipping_method"

    name: str
    active: bool | None = None
    position: int | None = None
    custom_fields: dict[str, Any] | None = None
    availability_rule_id: IdField | None = None
    media_id: IdField | None = None
    delivery_time_id: IdField
    tax_type: str
    tax_id: IdField | None = None
    description: str | None = None
    tracking_url: str | None = None
    technical_name: str | None
    translated: dict[str, Any] | None = None


class ShippingMethodRelations:
    delivery_time: ForeignRelation["DeliveryTime"]
    availability_rule: ForeignRelation["Rule"]
    media: ForeignRelation["Media"]
    tags: ManyRelation["Tag"]
    order_deliveries: ManyRelation["OrderDelivery"]
    sales_channels: ManyRelation["SalesChannel"]
    sales_channel_default_assignments: ManyRelation["SalesChannel"]
    tax: ForeignRelation["Tax"]

    """
    Todo:
    prices[ShippingMethodPrice], app_shipping_method[AppShippingMethod]
    """


class ShippingMethod(ShippingMethodBase["ShippingMethodEndpoint"], ShippingMethodRelations):
    pass


class ShippingMethodEndpoint(EndpointBase[ShippingMethod]):
    name = "shipping_method"
    path = "/shipping-method"
    model_class = ShippingMethod


from .delivery_time import DeliveryTime  # noqa: E402
from .media import Media  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .rule import Rule  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .tag import Tag  # noqa: E402
from .tax import Tax  # noqa: E402
