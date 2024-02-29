from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Media, Product


class ProductManufacturerBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_manufacturer"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    media_id: IdField | None = Field(
        default=None, serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId")
    )
    link: str | None = None
    name: str
    description: str | None = None
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


class ProductManufacturerRelations:
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")
    products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "products")


class ProductManufacturer(ProductManufacturerBase["ProductManufacturerEndpoint"], ProductManufacturerRelations):
    pass


class ProductManufacturerEndpoint(EndpointBase[ProductManufacturer]):
    name = "product_manufacturer"
    path = "/product-manufacturer"
    model_class = ProductManufacturer


registry.register_admin(ProductManufacturerEndpoint)
