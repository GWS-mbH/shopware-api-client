from typing import Any

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class QuoteDocumentBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_document"

    document_number: str | None = None
    document_type_id: IdField
    file_type: str
    quote_id: IdField
    quote_version_id: IdField | None = None
    config: dict[str, Any]
    sent: bool | None = None
    static: bool | None = None
    active: bool | None = None
    deep_link_code: str
    document_media_file_id: IdField | None = None
    document_a11y_media_file_id: IdField | None = None
