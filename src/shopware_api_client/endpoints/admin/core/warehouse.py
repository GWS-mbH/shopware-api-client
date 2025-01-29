from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class WarehouseBase(ApiModelBase[EndpointClass]):
    _identifier = "warehouse"

    name: str
    description: str | None = None


class WarehouseRelations:
    product_warehouses: ManyRelation["ProductWarehouse"]
    groups: ManyRelation["WarehouseGroup"]
    # order_products: ManyRelation["???"]


class Warehouse(WarehouseBase["WarehouseEndpoint"], WarehouseRelations):
    pass


class WarehouseEndpoint(EndpointBase[Warehouse]):
    name = "warehouse"
    path = "/warehouse"
    model_class = Warehouse


from .product_warehouse import ProductWarehouse  # noqa: E402
from .warehouse_group import WarehouseGroup  # noqa: E402
