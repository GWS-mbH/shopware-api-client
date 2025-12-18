from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.document import DocumentBase


class Document(DocumentBase, AdminModel["DocumentEndpoint"]):
    document_type: ForeignRelation["DocumentType"] = Field(default=...)
    order: ForeignRelation["Order"] = Field(default=...)
    referenced_document: ForeignRelation["Document"] = Field(default=...)
    dependent_documents: ManyRelation["Document"] = Field(default=...)
    document_media_file: ForeignRelation["Media"] = Field(default=...)


class DocumentEndpoint(AdminEndpoint[Document]):
    name = "document"
    path = "/document"
    model_class = Document


from .document_type import DocumentType  # noqa: E402
from .media import Media  # noqa: E402
from .order import Order  # noqa: E402
