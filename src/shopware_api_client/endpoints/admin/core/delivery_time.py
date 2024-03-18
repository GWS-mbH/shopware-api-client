from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class DeliveryTimeBase(ApiModelBase[EndpointClass]):
    _identifier: str = "delivery_time"

    name: str
    min: int
    max: int
    unit: str
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class DeliveryTimeRelations:
    shipping_methods: ManyRelation["ShippingMethod"]
    products: ManyRelation["Product"]


class DeliveryTime(DeliveryTimeBase["DeliveryTimeEndpoint"], DeliveryTimeRelations):
    pass


class DeliveryTimeEndpoint(EndpointBase[DeliveryTime]):
    name = "delivery_time"
    path = "/delivery-time"
    model_class = DeliveryTime


from .product import Product  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
