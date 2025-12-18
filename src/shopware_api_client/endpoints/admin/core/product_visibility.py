from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_visibility import ProductVisibilityBase


class ProductVisibility(ProductVisibilityBase, AdminModel["ProductVisibilityEndpoint"]):
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    product: ForeignRelation["Product"] = Field(default=...)


class ProductVisibilityEndpoint(AdminEndpoint[ProductVisibility]):
    name = "product_visibility"
    path = "/product-visibility"
    model_class = ProductVisibility


from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
