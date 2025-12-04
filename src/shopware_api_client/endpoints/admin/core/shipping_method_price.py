from shopware_api_client.endpoints.relations import ForeignRelation

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.models.shipping_method_price import ShippingMethodPriceBase


class ShippingMethodPrice(ShippingMethodPriceBase, AdminModel["ShippingMethodPriceEndpoint"]):
    shipping_method: ForeignRelation["ShippingMethod"]
    rule: ForeignRelation["Rule"]
    calculation_rule: ForeignRelation["Rule"]


class ShippingMethodPriceEndpoint(AdminEndpoint[ShippingMethodPrice]):
    name = "shipping_method_price"
    path = "/shipping-method-price"
    model_class = ShippingMethodPrice


from .shipping_method import ShippingMethod  # noqa: E402
from .rule import Rule  # noqa: E402
