from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Product, ProductCrossSelling


class ProductCrossSellingAssignedProductsBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_cross_selling_assigned_products"

    cross_selling_id: IdField = Field(
        ..., serialization_alias="crossSellingId", validation_alias=AliasChoices("cross_selling_id", "crossSellingId")
    )
    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    position: int | None = None
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class ProductCrossSellingAssignedProductsRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    cross_selling: ClassVar[ForeignRelation["ProductCrossSelling"]] = ForeignRelation(
        "ProductCrossSelling", "cross_selling_id"
    )


class ProductCrossSellingAssignedProducts(
    ProductCrossSellingAssignedProductsBase["ProductCrossSellingAssignedProductsEndpoint"],
    ProductCrossSellingAssignedProductsRelations,
):
    pass


class ProductCrossSellingAssignedProductsEndpoint(EndpointBase[ProductCrossSellingAssignedProducts]):
    name = "product_cross_selling_assigned_products"
    path = "/product-cross-selling-assigned-products"
    model_class = ProductCrossSellingAssignedProducts


registry.register_admin(ProductCrossSellingAssignedProductsEndpoint)
