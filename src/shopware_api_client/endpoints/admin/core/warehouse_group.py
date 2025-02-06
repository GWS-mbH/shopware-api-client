from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class WarehouseGroupBase(ApiModelBase[EndpointClass]):
    _identifier = "warehouse_group"
    
    name: str
    description: str | None = None
    priority: int | None = None
    rule_id: IdField | None = None
    

class WarehouseGroupRelations:
    warehouses: ManyRelation["Warehouse"]
    products: ManyRelation["Product"]
    rule: ForeignRelation["Rule"]


class WarehouseGroup(WarehouseGroupBase["WarehouseGroupEndpoint"], WarehouseGroupRelations):
    pass


class WarehouseGroupEndpoint(EndpointBase[WarehouseGroup]):
    name = "warehouse_group"
    path = "/warehouse-group"
    model_class = WarehouseGroup

from .product import Product  # noqa: E402
from .rule import Rule  # noqa: E402
from .warehouse import Warehouse  # noqa: E402
