from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.unit import Unit as UnitBase


class Unit(UnitBase, AdminModel["UnitEndpoint"]):
    products: ManyRelation["Product"]


class UnitEndpoint(AdminEndpoint[Unit]):
    name = "unit"
    path = "/unit"
    model_class = Unit


from .product import Product  # noqa: E402
