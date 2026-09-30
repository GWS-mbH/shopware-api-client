from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.quote_document import QuoteDocumentBase


class QuoteDocument(QuoteDocumentBase, AdminModel["QuoteDocumentEndpoint"]):
    document_type: ForeignRelation["DocumentType"] = Field(default=...)
    quote: ForeignRelation["Quote"] = Field(default=...)
    document_media_file: ForeignRelation["Media"] = Field(default=...)
    document_a11y_media_file: ForeignRelation["Media"] = Field(default=...)


class QuoteDocumentEndpoint(AdminEndpoint[QuoteDocument]):
    name = "quote_document"
    path = "/quote-document"
    model_class = QuoteDocument


from ..core.document_type import DocumentType  # noqa: E402
from ..core.media import Media  # noqa: E402
from .quote import Quote  # noqa: E402
