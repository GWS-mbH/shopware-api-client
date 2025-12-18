from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.warehouse_group import WarehouseGroupBase


class WarehouseGroup(WarehouseGroupBase, AdminModel["WarehouseGroupEndpoint"]):
    warehouses: ManyRelation["Warehouse"] = Field(default=...)
    products: ManyRelation["Product"] = Field(default=...)
    rule: ForeignRelation["Rule"] = Field(default=...)


class WarehouseGroupEndpoint(AdminEndpoint[WarehouseGroup]):
    name = "warehouse_group"
    path = "/warehouse-group"
    model_class = WarehouseGroup


from .product import Product  # noqa: E402
from .rule import Rule  # noqa: E402
from .warehouse import Warehouse  # noqa: E402
