from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_warehouse import ProductWarehouseBase


class ProductWarehouse(ProductWarehouseBase, AdminModel["ProductWarehouseEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    warehouse: ForeignRelation["Warehouse"] = Field(default=...)


class ProductWarehouseEndpoint(AdminEndpoint[ProductWarehouse]):
    name = "product_warehouse"
    path = "/product-warehouse"
    model_class = ProductWarehouse


from .product import Product  # noqa: E402
from .warehouse import Warehouse  # noqa: E402
