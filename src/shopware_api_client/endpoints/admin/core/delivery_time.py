from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.delivery_time import DeliveryTimeBase


class DeliveryTime(DeliveryTimeBase, AdminModel["DeliveryTimeEndpoint"]):
    shipping_methods: ManyRelation["ShippingMethod"] = Field(default=...)
    products: ManyRelation["Product"] = Field(default=...)


class DeliveryTimeEndpoint(AdminEndpoint[DeliveryTime]):
    name = "delivery_time"
    path = "/delivery-time"
    model_class = DeliveryTime


from .product import Product  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
