from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class UnitBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "unit"

    short_code: str
    name: str
