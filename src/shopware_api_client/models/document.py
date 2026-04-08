from typing import Any

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class DocumentBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "document"

    document_type_id: IdField
    file_type: str
    referenced_document_id: IdField | None = None
    order_id: IdField
    document_media_file_id: IdField | None = None
    order_version_id: IdField | None = None
    config: dict[str, Any]
    sent: bool | None = None
    static: bool | None = None
    deep_link_code: str
    document_number: str | None = None
