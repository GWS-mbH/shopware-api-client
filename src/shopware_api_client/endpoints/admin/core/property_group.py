from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import PropertyGroupOption


class PropertyGroupBase(ApiModelBase[EndpointClass]):
    _identifier: str = "property_group"

    name: str
    description: str | None = None
    display_type: str = Field(
        ..., serialization_alias="displayType", validation_alias=AliasChoices("display_type", "displayType")
    )
    sorting_type: str = Field(
        ..., serialization_alias="sortingType", validation_alias=AliasChoices("sorting_type", "sortingType")
    )
    filterable: bool | None = None
    visible_on_product_detail_page: bool | None = Field(
        default=None,
        serialization_alias="visibleOnProductDetailPage",
        validation_alias=AliasChoices("visible_on_product_detail_page", "visibleOnProductDetailPage"),
    )
    position: int | None = None
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


class PropertyGroupRelations:
    options: ClassVar[ManyRelation["PropertyGroupOption"]] = ManyRelation("PropertyGroupOption", "options")


class PropertyGroup(PropertyGroupBase["PropertyGroupEndpoint"], PropertyGroupRelations):
    pass


class PropertyGroupEndpoint(EndpointBase[PropertyGroup]):
    name = "property_group"
    path = "/property-group"
    model_class = PropertyGroup


registry.register_admin(PropertyGroupEndpoint)
