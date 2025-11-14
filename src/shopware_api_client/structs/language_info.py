from shopware_api_client.fieldsets import FieldSetBase


class LanguageInfo(FieldSetBase):
    name: str
    locale_code: str
