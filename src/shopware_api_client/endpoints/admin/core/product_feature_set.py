from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.product_feature_set import ProductFeatureSetBase


class ProductFeatureSet(ProductFeatureSetBase, AdminModel["ProductFeatureSetEndpoint"]):
    products: ManyRelation["Product"] = Field(default=...)


class ProductFeatureSetEndpoint(AdminEndpoint[ProductFeatureSet]):
    name = "product_feature_set"
    path = "/product-feature-set"
    model_class = ProductFeatureSet


from .product import Product  # noqa: E402
