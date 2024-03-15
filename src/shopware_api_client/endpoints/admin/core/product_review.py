from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductReviewBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_review"

    product_id: IdField
    product_version_id: IdField | None = None
    customer_id: IdField | None = None
    sales_channel_id: IdField
    language_id: IdField
    external_user: str | None = None
    external_email: str | None = None
    title: str
    content: str
    points: float | None = None
    status: bool | None = None
    comment: str | None = None
    custom_fields: dict[str, Any] | None = None


class ProductReviewRelations:
    product: ForeignRelation["Product"]
    customer: ForeignRelation["Customer"]
    sales_channel: ForeignRelation["SalesChannel"]
    language: ForeignRelation["Language"]


class ProductReview(ProductReviewBase["ProductReviewEndpoint"], ProductReviewRelations):
    pass


class ProductReviewEndpoint(EndpointBase[ProductReview]):
    name = "product_review"
    path = "/product-review"
    model_class = ProductReview


from .customer import Customer  # noqa: E402
from .language import Language  # noqa: E402
from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
