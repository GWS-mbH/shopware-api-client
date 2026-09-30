from typing import Annotated, Any

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class QuoteDocumentBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_document"

    document_number: str | None = None
    document_type_id: Annotated[IdField, RefersTo("document_type")]
    file_type: str
    quote_id: Annotated[IdField, RefersTo("quote")]
    quote_version_id: IdField | None = None
    config: dict[str, Any]
    sent: bool | None = None
    static: bool | None = None
    active: bool | None = None
    deep_link_code: str
    document_media_file_id: Annotated[IdField | None, RefersTo("media")] = None
    document_a11y_media_file_id: Annotated[IdField | None, RefersTo("media")] = None
