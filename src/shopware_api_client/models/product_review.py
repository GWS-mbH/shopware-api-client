from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductReviewBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_review"

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    customer_id: Annotated[IdField | None, RefersTo("customer")] = None
    sales_channel_id: Annotated[IdField, RefersTo("sales_channel")]
    language_id: Annotated[IdField, RefersTo("language")]
    external_user: str | None = None
    external_email: str | None = None
    title: str
    content: str
    points: float | None = None
    status: bool | None = None
    comment: str | None = None
