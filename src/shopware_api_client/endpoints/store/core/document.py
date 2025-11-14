from shopware_api_client.models.document import DocumentBase


class Document(DocumentBase):
    document_type: "DocumentType | None" = None
    order: "Order | None" = None
    referenced_document: "Document | None" = None
    dependent_documents: list["Document"] | None = None
    document_media_file: "Media | None" = None
    document_a11y_media_file: "Media | None" = None


from .document_type import DocumentType  # noqa: E402
from .media import Media  # noqa: E402
from .order import Order  # noqa: E402
