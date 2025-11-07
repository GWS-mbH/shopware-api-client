from shopware_api_client.base import ApiModelBase


class Tag(ApiModelBase):
    _identifier: str = "tag"

    name: str
