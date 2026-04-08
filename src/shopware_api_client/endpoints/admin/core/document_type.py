from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.document_type import DocumentTypeBase


class DocumentType(DocumentTypeBase, AdminModel["DocumentTypeEndpoint"]):
    documents: ManyRelation["Document"] = Field(default=...)
    document_base_configs: ManyRelation["DocumentBaseConfig"] = Field(default=...)
    document_base_config_sales_channels: ManyRelation["DocumentBaseConfigSalesChannel"] = Field(default=...)


class DocumentTypeEndpoint(AdminEndpoint[DocumentType]):
    name = "document_type"
    path = "/document-type"
    model_class = DocumentType


from .document import Document  # noqa: E402
from .document_base_config import DocumentBaseConfig  # noqa: E402
from .document_base_config_sales_channel import DocumentBaseConfigSalesChannel  # noqa: E402
