from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.product_manufacturer import ProductManufacturerBase


class ProductManufacturer(ProductManufacturerBase, AdminModel["ProductManufacturerEndpoint"]):
    media: ForeignRelation["Media"] = Field(default=...)
    products: ManyRelation["Product"] = Field(default=...)


class ProductManufacturerEndpoint(AdminEndpoint[ProductManufacturer]):
    name = "product_manufacturer"
    path = "/product-manufacturer"
    model_class = ProductManufacturer


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
