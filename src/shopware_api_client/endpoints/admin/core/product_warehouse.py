from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductWarehouseBase(ApiModelBase[EndpointClass]):
    _identifier = "product_warehouse"

    stock: int
    product_id: IdField
    warehouse_id: IdField


class ProductWarehouseRelations:
    product: ForeignRelation["Product"]
    warehouse: ForeignRelation["Warehouse"]


class ProductWarehouse(ProductWarehouseBase["ProductWarehouseEndpoint"], ProductWarehouseRelations):
    pass


class ProductWarehouseEndpoint(EndpointBase[ProductWarehouse]):
    name = "product_warehouse"
    path = "/product-warehouse"
    model_class = ProductWarehouse


from .product import Product  # noqa: E402
from .warehouse import Warehouse  # noqa: E402
