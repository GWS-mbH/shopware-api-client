from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.tax import TaxBase


class Tax(TaxBase, AdminModel["TaxEndpoint"]):
    products: ManyRelation["Product"]
    rules: ManyRelation["Rule"]
    shipping_methods: ManyRelation["ShippingMethod"]


class TaxEndpoint(AdminEndpoint[Tax]):
    name = "tax"
    path = "/tax"
    model_class = Tax


from .product import Product  # noqa: E402
from .rule import Rule  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
