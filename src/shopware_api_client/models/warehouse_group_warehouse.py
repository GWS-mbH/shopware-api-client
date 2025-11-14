from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class WarehouseGroupWarehouseBase(ApiModelBase):
    _identifier = "warehouse_group_warehouse"

    name: str
    warehouse_id: IdField
    warehouse_group_id: IdField
    priority: int | None = None
