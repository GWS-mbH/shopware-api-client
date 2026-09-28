from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class MainCategoryBase(ApiModelBase):
    _identifier: str = "main_category"

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    category_id: Annotated[IdField, RefersTo("category")]
    category_version_id: IdField | None = None
    sales_channel_id: Annotated[IdField, RefersTo("sales_channel")]
