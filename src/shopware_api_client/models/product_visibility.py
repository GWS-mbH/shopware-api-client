from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductVisibilityBase(ApiModelBase):
    _identifier: str = "product_visibility"

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    sales_channel_id: Annotated[IdField, RefersTo("sales_channel")]
    visibility: int
