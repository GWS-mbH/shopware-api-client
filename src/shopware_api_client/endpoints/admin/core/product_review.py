from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_review import ProductReviewBase


class ProductReview(ProductReviewBase, AdminModel["ProductReviewEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    customer: ForeignRelation["Customer"] = Field(default=...)
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    language: ForeignRelation["Language"] = Field(default=...)


class ProductReviewEndpoint(AdminEndpoint[ProductReview]):
    name = "product_review"
    path = "/product-review"
    model_class = ProductReview


from .customer import Customer  # noqa: E402
from .language import Language  # noqa: E402
from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
