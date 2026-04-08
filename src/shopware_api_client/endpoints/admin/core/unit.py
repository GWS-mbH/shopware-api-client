from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.unit import UnitBase


class Unit(UnitBase, AdminModel["UnitEndpoint"]):
    products: ManyRelation["Product"] = Field(default=...)


class UnitEndpoint(AdminEndpoint[Unit]):
    name = "unit"
    path = "/unit"
    model_class = Unit


from .product import Product  # noqa: E402
