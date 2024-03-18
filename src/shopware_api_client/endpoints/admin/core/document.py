from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class DocumentBase(ApiModelBase[EndpointClass]):
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
    custom_fields: dict[str, Any] | None = None


class DocumentRelations:
    document_type: ForeignRelation["DocumentType"]
    order: ForeignRelation["Order"]
    referenced_document: ForeignRelation["Document"]
    dependent_documents: ManyRelation["Document"]
    document_media_file: ForeignRelation["Media"]


class Document(DocumentBase["DocumentEndpoint"], DocumentRelations):
    pass


class DocumentEndpoint(EndpointBase[Document]):
    name = "document"
    path = "/document"
    model_class = Document


from .document_type import DocumentType  # noqa: E402
from .media import Media  # noqa: E402
from .order import Order  # noqa: E402
