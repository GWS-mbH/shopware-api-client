from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class LanguageBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "language"

    parent_id: Annotated[IdField | None, RefersTo("language")] = None
    locale_id: Annotated[IdField, RefersTo("locale")]
    translation_code_id: Annotated[IdField | None, RefersTo("locale")] = None
    name: str
