from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class ProductCrossSellingBase(ApiModelBase):
    _identifier: str = "product_cross_selling"

    name: str
    position: int
    sort_by: str | None = None
    sort_direction: str | None = None
    type: str
    active: bool | None = None
    limit: int | None = None
    product_id: IdField
    product_version_id: IdField | None = None
    product_stream_id: IdField | None = None
