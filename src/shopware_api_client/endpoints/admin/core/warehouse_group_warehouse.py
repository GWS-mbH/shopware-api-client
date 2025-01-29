from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ManyRelation


class WarehouseGroupWarehouseBase(ApiModelBase[EndpointClass]):
    _identifier = "warehouse_group_warehouse"
    
    name: str
    warehouse_id: IdField
    warehouse_group_id: IdField
    priority: int | None = None
    

class WarehouseGroupWarehouseRelations:
    warehouses: ManyRelation["Warehouse"]
    warehouse_group: ManyRelation["WarehouseGroup"]


class WarehouseGroupWarehouse(WarehouseGroupWarehouseBase["WarehouseGroupWarehouseEndpoint"], WarehouseGroupWarehouseRelations):
    pass


class WarehouseGroupWarehouseEndpoint(EndpointBase[WarehouseGroupWarehouse]):
    name = "warehouse_group_warehouse"
    path = "/warehouse-group-warehouse"
    model_class = WarehouseGroupWarehouse

from .warehouse import Warehouse  # noqa: E402
from .warehouse_group import WarehouseGroup  # noqa: E402
