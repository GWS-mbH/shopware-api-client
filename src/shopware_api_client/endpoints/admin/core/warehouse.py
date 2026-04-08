from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.warehouse import WarehouseBase


class Warehouse(WarehouseBase, AdminModel["WarehouseEndpoint"]):
    product_warehouses: ManyRelation["ProductWarehouse"] = Field(default=...)
    groups: ManyRelation["WarehouseGroup"] = Field(default=...)
    # order_products: ManyRelation["???"]


class WarehouseEndpoint(AdminEndpoint[Warehouse]):
    name = "warehouse"
    path = "/warehouse"
    model_class = Warehouse


from .product_warehouse import ProductWarehouse  # noqa: E402
from .warehouse_group import WarehouseGroup  # noqa: E402
