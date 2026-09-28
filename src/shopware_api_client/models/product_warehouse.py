from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductWarehouseBase(ApiModelBase):
    _identifier = "product_warehouse"

    stock: int
    product_id: Annotated[IdField, RefersTo("product")]
    warehouse_id: Annotated[IdField, RefersTo("warehouse")]
