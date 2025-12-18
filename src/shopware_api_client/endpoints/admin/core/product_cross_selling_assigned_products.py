from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_cross_selling_assigned_products import ProductCrossSellingAssignedProductsBase


class ProductCrossSellingAssignedProducts(
    ProductCrossSellingAssignedProductsBase, AdminModel["ProductCrossSellingAssignedProductsEndpoint"]
):
    product: ForeignRelation["Product"] = Field(default=...)
    cross_selling: ForeignRelation["ProductCrossSelling"] = Field(default=...)


class ProductCrossSellingAssignedProductsEndpoint(AdminEndpoint[ProductCrossSellingAssignedProducts]):
    name = "product_cross_selling_assigned_products"
    path = "/product-cross-selling-assigned-products"
    model_class = ProductCrossSellingAssignedProducts


from .product import Product  # noqa: E402
from .product_cross_selling import ProductCrossSelling  # noqa: E402
