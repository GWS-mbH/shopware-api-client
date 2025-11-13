from shopware_api_client.base import ApiModelBase


class WarehouseBase(ApiModelBase):
    _identifier = "warehouse"

    name: str
    description: str | None = None
