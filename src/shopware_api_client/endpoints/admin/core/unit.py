from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class UnitBase(ApiModelBase[EndpointClass]):
    _identifier: str = "unit"

    short_code: str
    name: str
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class UnitRelations:
    products: ManyRelation["Product"]


class Unit(UnitBase["UnitEndpoint"], UnitRelations):
    pass


class UnitEndpoint(EndpointBase[Unit]):
    name = "unit"
    path = "/unit"
    model_class = Unit


from .product import Product  # noqa: E402
