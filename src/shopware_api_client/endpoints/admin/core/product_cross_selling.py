from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Product, ProductCrossSellingAssignedProducts, ProductStream


class ProductCrossSellingBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_cross_selling"

    name: str
    position: int
    sort_by: str | None = Field(
        default=None, serialization_alias="sortBy", validation_alias=AliasChoices("sort_by", "sortBy")
    )
    sort_direction: str | None = Field(
        default=None,
        serialization_alias="sortDirection",
        validation_alias=AliasChoices("sort_direction", "sortDirection"),
    )
    type: str
    active: bool | None = None
    limit: int | None = None
    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    product_stream_id: IdField | None = Field(
        default=None,
        serialization_alias="productStreamId",
        validation_alias=AliasChoices("product_stream_id", "productStreamId"),
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


class ProductCrossSellingRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    product_stream: ClassVar[ForeignRelation["ProductStream"]] = ForeignRelation("ProductStream", "product_stream_id")
    assigned_products: ClassVar[ManyRelation["ProductCrossSellingAssignedProducts"]] = ManyRelation(
        "ProductCrossSellingAssignedProducts", "assignedProducts"
    )


class ProductCrossSelling(ProductCrossSellingBase["ProductCrossSellingEndpoint"], ProductCrossSellingRelations):
    pass


class ProductCrossSellingEndpoint(EndpointBase[ProductCrossSelling]):
    name = "product_cross_selling"
    path = "/product-cross-selling"
    model_class = ProductCrossSelling


registry.register_admin(ProductCrossSellingEndpoint)
