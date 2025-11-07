from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.product_cross_selling import ProductCrossSelling as ProductCrossSellingBase


class ProductCrossSelling(ProductCrossSellingBase, AdminModel["ProductCrossSellingEndpoint"]):
    product: ForeignRelation["Product"]
    product_stream: ForeignRelation["ProductStream"]
    assigned_products: ManyRelation["ProductCrossSellingAssignedProducts"]


class ProductCrossSellingEndpoint(AdminEndpoint[ProductCrossSelling]):
    name = "product_cross_selling"
    path = "/product-cross-selling"
    model_class = ProductCrossSelling


from .product import Product  # noqa: E402
from .product_cross_selling_assigned_products import ProductCrossSellingAssignedProducts  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
