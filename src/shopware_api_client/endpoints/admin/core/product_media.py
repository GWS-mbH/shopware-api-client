from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Media, Product


class ProductMediaBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_media"

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
    media_id: IdField = Field(..., serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId"))
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


class ProductMediaRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")
    cover_products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "coverProducts")


class ProductMedia(ProductMediaBase["ProductMediaEndpoint"], ProductMediaRelations):
    pass


class ProductMediaEndpoint(EndpointBase[ProductMedia]):
    name = "product_media"
    path = "/product-media"
    model_class = ProductMedia


registry.register_admin(ProductMediaEndpoint)
