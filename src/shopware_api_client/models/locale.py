from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class LocaleBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "locale"

    code: str
    name: str
    territory: str
