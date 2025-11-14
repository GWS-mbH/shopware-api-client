from shopware_api_client.base import ApiModelBase


class TagBase(ApiModelBase):
    _identifier: str = "tag"

    name: str
