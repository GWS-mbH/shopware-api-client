from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Media, Product, ProductConfiguratorSetting, PropertyGroup


class PropertyGroupOptionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "property_group_option"

    group_id: IdField = Field(..., serialization_alias="groupId", validation_alias=AliasChoices("group_id", "groupId"))
    name: str
    position: int | None = None
    color_hex_code: str | None = Field(
        default=None,
        serialization_alias="colorHexCode",
        validation_alias=AliasChoices("color_hex_code", "colorHexCode"),
    )
    media_id: IdField | None = Field(
        default=None, serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId")
    )
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


class PropertyGroupOptionRelations:
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")
    group: ClassVar[ForeignRelation["PropertyGroup"]] = ForeignRelation("PropertyGroup", "group_id")
    product_configurator_settings: ClassVar[ManyRelation["ProductConfiguratorSetting"]] = ManyRelation(
        "ProductConfiguratorSetting", "productConfiguratorSettings"
    )
    product_properties: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "productProperties")
    product_options: ClassVar[ManyRelation["Product"]] = ManyRelation("ProductOption", "productOptions")


class PropertyGroupOption(PropertyGroupOptionBase["PropertyGroupOptionEndpoint"], PropertyGroupOptionRelations):
    pass


class PropertyGroupOptionEndpoint(EndpointBase[PropertyGroupOption]):
    name = "property_group_option"
    path = "/property-group-option"
    model_class = PropertyGroupOption


registry.register_admin(PropertyGroupOptionEndpoint)
