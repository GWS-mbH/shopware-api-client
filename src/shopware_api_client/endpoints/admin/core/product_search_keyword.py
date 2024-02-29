from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Language, Product


class ProductSearchKeywordBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_search_keyword"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    language_id: IdField = Field(
        ..., serialization_alias="languageId", validation_alias=AliasChoices("language_id", "languageId")
    )
    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    keyword: str
    ranking: float
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class ProductSearchKeywordRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    language: ClassVar[ForeignRelation["Language"]] = ForeignRelation("Language", "language_id")


class ProductSearchKeyword(ProductSearchKeywordBase["ProductSearchKeywordEndpoint"], ProductSearchKeywordRelations):
    pass


class ProductSearchKeywordEndpoint(EndpointBase[ProductSearchKeyword]):
    name = "product_search_keyword"
    path = "/product-search-keyword"
    model_class = ProductSearchKeyword


registry.register_admin(ProductSearchKeywordEndpoint)
