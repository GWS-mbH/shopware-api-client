from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class ProductReviewBase(ApiModelBase, CustomFieldsMixin):
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
