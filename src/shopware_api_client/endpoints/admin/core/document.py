from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.document import DocumentBase


class Document(DocumentBase, AdminModel["DocumentEndpoint"]):
    document_type: ForeignRelation["DocumentType"]
    order: ForeignRelation["Order"]
    referenced_document: ForeignRelation["Document"]
    dependent_documents: ManyRelation["Document"]
    document_media_file: ForeignRelation["Media"]


class DocumentEndpoint(AdminEndpoint[Document]):
    name = "document"
    path = "/document"
    model_class = Document


from .document_type import DocumentType  # noqa: E402
from .media import Media  # noqa: E402
from .order import Order  # noqa: E402
