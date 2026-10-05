from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class WarehouseGroupWarehouseBase(ApiModelBase):
    _identifier = "warehouse_group_warehouse"

    name: str
    warehouse_id: Annotated[IdField, RefersTo("warehouse")]
    warehouse_group_id: Annotated[IdField, RefersTo("warehouse_group")]
    priority: int | None = None
