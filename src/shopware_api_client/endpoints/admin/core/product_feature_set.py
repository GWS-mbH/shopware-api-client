from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class ProductFeatureSetBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_feature_set"

    name: str
    description: str | None = None
    features: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class ProductFeatureSetRelations:
    products: ManyRelation["Product"]


class ProductFeatureSet(ProductFeatureSetBase["ProductFeatureSetEndpoint"], ProductFeatureSetRelations):
    pass


class ProductFeatureSetEndpoint(EndpointBase[ProductFeatureSet]):
    name = "product_feature_set"
    path = "/product-feature-set"
    model_class = ProductFeatureSet


from .product import Product  # noqa: E402
