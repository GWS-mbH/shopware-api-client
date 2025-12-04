from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class ProductVisibilityBase(ApiModelBase):
    _identifier: str = "product_visibility"

    product_id: IdField
    product_version_id: IdField | None = None
    sales_channel_id: IdField
    visibility: int
