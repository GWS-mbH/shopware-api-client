from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Product, SalesChannel


class ProductVisibilityBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_visibility"

    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    sales_channel_id: IdField = Field(
        ..., serialization_alias="salesChannelId", validation_alias=AliasChoices("sales_channel_id", "salesChannelId")
    )
    visibility: int
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class ProductVisibilityRelations:
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")


class ProductVisibility(ProductVisibilityBase["ProductVisibilityEndpoint"], ProductVisibilityRelations):
    pass


class ProductVisibilityEndpoint(EndpointBase[ProductVisibility]):
    name = "product_visibility"
    path = "/product-visibility"
    model_class = ProductVisibility


registry.register_admin(ProductVisibilityEndpoint)
