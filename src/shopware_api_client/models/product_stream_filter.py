from typing import Annotated, Any

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductStreamFilterBase(ApiModelBase):
    _identifier: str = "product_stream_filter"

    product_stream_id: Annotated[IdField, RefersTo("product_stream")]
    parent_id: Annotated[IdField | None, RefersTo("product_stream_filter")] = None
    type: str
    field: str | None = None
    operator: str | None = None
    value: str | None = None
    parameters: dict[str, Any] | None = None
    position: int | None = None
