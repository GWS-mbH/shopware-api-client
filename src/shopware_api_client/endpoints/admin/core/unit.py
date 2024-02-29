from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Product


class UnitBase(ApiModelBase[EndpointClass]):
    _identifier: str = "unit"

    short_code: str = Field(
        ..., serialization_alias="shortCode", validation_alias=AliasChoices("short_code", "shortCode")
    )
    name: str
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )
    translated: dict[str, Any] | None = None


class UnitRelations:
    products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "products")


class Unit(UnitBase["UnitEndpoint"], UnitRelations):
    pass


class UnitEndpoint(EndpointBase[Unit]):
    name = "unit"
    path = "/unit"
    model_class = Unit


registry.register_admin(UnitEndpoint)
