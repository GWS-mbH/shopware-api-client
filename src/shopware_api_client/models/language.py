from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class LanguageBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "language"

    parent_id: IdField | None = None
    locale_id: IdField
    translation_code_id: IdField | None = None
    name: str
