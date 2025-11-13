from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class MainCategoryBase(ApiModelBase):
    _identifier: str = "main_category"

    product_id: IdField
    product_version_id: IdField | None = None
    category_id: IdField
    category_version_id: IdField | None = None
    sales_channel_id: IdField
