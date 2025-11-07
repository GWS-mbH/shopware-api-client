from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class Locale(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "locale"

    code: str
    name: str
    territory: str
