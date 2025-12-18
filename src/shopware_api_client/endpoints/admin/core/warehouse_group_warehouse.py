from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.warehouse_group_warehouse import WarehouseGroupWarehouseBase


class WarehouseGroupWarehouse(WarehouseGroupWarehouseBase, AdminModel["WarehouseGroupWarehouseEndpoint"]):
    warehouses: ManyRelation["Warehouse"] = Field(default=...)
    warehouse_group: ManyRelation["WarehouseGroup"] = Field(default=...)


class WarehouseGroupWarehouseEndpoint(AdminEndpoint[WarehouseGroupWarehouse]):
    name = "warehouse_group_warehouse"
    path = "/warehouse-group-warehouse"
    model_class = WarehouseGroupWarehouse


from .warehouse import Warehouse  # noqa: E402
from .warehouse_group import WarehouseGroup  # noqa: E402
