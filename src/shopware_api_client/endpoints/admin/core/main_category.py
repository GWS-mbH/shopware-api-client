from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Category, Product, SalesChannel


class MainCategoryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "main_category"

    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    category_id: IdField = Field(
        ..., serialization_alias="categoryId", validation_alias=AliasChoices("category_id", "categoryId")
    )
    category_version_id: IdField | None = Field(
        default=None,
        serialization_alias="categoryVersionId",
        validation_alias=AliasChoices("category_version_id", "categoryVersionId"),
    )
    sales_channel_id: IdField = Field(
        ..., serialization_alias="salesChannelId", validation_alias=AliasChoices("sales_channel_id", "salesChannelId")
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


class MainCategoryRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    category: ClassVar[ForeignRelation["Category"]] = ForeignRelation("Category", "category_id")
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")


class MainCategory(MainCategoryBase["MainCategoryEndpoint"], MainCategoryRelations):
    pass


class MainCategoryEndpoint(EndpointBase[MainCategory]):
    name = "main_category"
    path = "/main-category"
    model_class = MainCategory


registry.register_admin(MainCategoryEndpoint)
