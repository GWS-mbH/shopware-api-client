from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductCrossSellingBase(ApiModelBase):
    _identifier: str = "product_cross_selling"

    name: str
    position: int
    sort_by: str | None = None
    sort_direction: str | None = None
    type: str
    active: bool | None = None
    limit: int | None = None
    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    product_stream_id: Annotated[IdField | None, RefersTo("product_stream")] = None
