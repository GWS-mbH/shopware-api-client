from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.product_cross_selling import ProductCrossSellingBase


class ProductCrossSelling(ProductCrossSellingBase, AdminModel["ProductCrossSellingEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    product_stream: ForeignRelation["ProductStream"] = Field(default=...)
    assigned_products: ManyRelation["ProductCrossSellingAssignedProducts"] = Field(default=...)


class ProductCrossSellingEndpoint(AdminEndpoint[ProductCrossSelling]):
    name = "product_cross_selling"
    path = "/product-cross-selling"
    model_class = ProductCrossSelling


from .product import Product  # noqa: E402
from .product_cross_selling_assigned_products import ProductCrossSellingAssignedProducts  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
