from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_price import ProductPriceBase


class ProductPrice(ProductPriceBase, AdminModel["ProductPriceEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    rule: ForeignRelation["Rule"] = Field(default=...)


class ProductPriceEndpoint(AdminEndpoint[ProductPrice]):
    name = "product_price"
    path = "/product-price"
    model_class = ProductPrice


from .product import Product  # noqa: E402
from .rule import Rule  # noqa: E402
