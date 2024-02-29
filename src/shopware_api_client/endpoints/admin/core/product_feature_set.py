from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Product


class ProductFeatureSetBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_feature_set"

    name: str
    description: str | None = None
    features: dict[str, Any] | None = None
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


class ProductFeatureSetRelations:
    products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "products")


class ProductFeatureSet(ProductFeatureSetBase["ProductFeatureSetEndpoint"], ProductFeatureSetRelations):
    pass


class ProductFeatureSetEndpoint(EndpointBase[ProductFeatureSet]):
    name = "product_feature_set"
    path = "/product-feature-set"
    model_class = ProductFeatureSet


registry.register_admin(ProductFeatureSetEndpoint)
