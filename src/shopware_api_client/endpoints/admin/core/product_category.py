from pydantic import AliasChoices, Field
from typing import TYPE_CHECKING, ClassVar

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Product, Category


class ProductCategoryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_category"

    product_id: IdField | None = Field(
        default=None, serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    category_id: IdField | None = Field(
        default=None, serialization_alias="categoryId", validation_alias=AliasChoices("category_id", "categoryId")
    )

    category_version_id: IdField | None = Field(
        default=None,
        serialization_alias="categoryVersionId",
        validation_alias=AliasChoices("category_version_id", "categoryVersionId"),
    )


class ProductCategoryRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    category: ClassVar[ForeignRelation["Category"]] = ForeignRelation("Category", "category_id")


class ProductCategory(ProductCategoryBase["ProductCategoryEndpoint"], ProductCategoryRelations):
    pass


class ProductCategoryEndpoint(EndpointBase[ProductCategory]):
    name = "product_category"
    path = ""
    model_class = ProductCategory


registry.register_admin(ProductCategoryEndpoint)
