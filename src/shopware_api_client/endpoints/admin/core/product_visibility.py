from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_visibility import ProductVisibility as ProductVisibilityBase


class ProductVisibility(ProductVisibilityBase, AdminModel["ProductVisibilityEndpoint"]):
    sales_channel: ForeignRelation["SalesChannel"]
    product: ForeignRelation["Product"]


class ProductVisibilityEndpoint(AdminEndpoint[ProductVisibility]):
    name = "product_visibility"
    path = "/product-visibility"
    model_class = ProductVisibility


from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
