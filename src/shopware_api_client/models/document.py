from typing import Annotated, Any

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class DocumentBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "document"

    document_type_id: Annotated[IdField, RefersTo("document_type")]
    file_type: str
    referenced_document_id: Annotated[IdField | None, RefersTo("document")] = None
    order_id: Annotated[IdField, RefersTo("order")]
    document_media_file_id: Annotated[IdField | None, RefersTo("media")] = None
    order_version_id: IdField | None = None
    config: dict[str, Any]
    sent: bool | None = None
    static: bool | None = None
    deep_link_code: str
    document_number: str | None = None
