from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Category, ProductCrossSelling, ProductExport


class ProductStreamBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_stream"

    api_filter: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="apiFilter",
        validation_alias=AliasChoices("api_filter", "apiFilter"),
        exclude=True,
    )
    invalid: bool | None = Field(default=None, exclude=True)
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


class ProductStreamRelations:
    product_cross_sellings: ClassVar[ManyRelation["ProductCrossSelling"]] = ManyRelation(
        "ProductCrossSelling", "productCrossSellings"
    )
    product_exports: ClassVar[ManyRelation["ProductExport"]] = ManyRelation("ProductExport", "productExports")
    categories: ClassVar[ManyRelation["Category"]] = ManyRelation("Category", "categories")

    """
    Todo:
    filters[ProductStreamFilter]
    """


class ProductStream(ProductStreamBase["ProductStreamEndpoint"], ProductStreamRelations):
    pass


class ProductStreamEndpoint(EndpointBase[ProductStream]):
    name = "product_stream"
    path = "/product-stream"
    model_class = ProductStream


registry.register_admin(ProductStreamEndpoint)
