from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class WarehouseGroupBase(ApiModelBase):
    _identifier = "warehouse_group"

    name: str
    description: str | None = None
    priority: int | None = None
    rule_id: IdField | None = None
