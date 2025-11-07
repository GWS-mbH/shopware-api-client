from shopware_api_client.base import ApiModelBase


class Warehouse(ApiModelBase):
    _identifier = "warehouse"

    name: str
    description: str | None = None
