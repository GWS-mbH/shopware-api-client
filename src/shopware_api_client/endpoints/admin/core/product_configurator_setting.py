from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Media, Product, PropertyGroupOption


class ProductConfiguratorSettingBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_configurator_setting"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    media_id: IdField | None = Field(
        default=None, serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId")
    )
    option_id: IdField = Field(
        ..., serialization_alias="optionId", validation_alias=AliasChoices("option_id", "optionId")
    )
    price: dict[str, Any] | None = None
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


class ProductConfiguratorSettingRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")
    option: ClassVar[ForeignRelation["PropertyGroupOption"]] = ForeignRelation("PropertyGroupOption", "option_id")


class ProductConfiguratorSetting(
    ProductConfiguratorSettingBase["ProductConfiguratorSettingEndpoint"], ProductConfiguratorSettingRelations
):
    pass


class ProductConfiguratorSettingEndpoint(EndpointBase[ProductConfiguratorSetting]):
    name = "product_configurator_setting"
    path = "/product-configurator-setting"
    model_class = ProductConfiguratorSetting


registry.register_admin(ProductConfiguratorSettingEndpoint)
