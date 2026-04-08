from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.document_base_config import DocumentBaseConfigBase


class DocumentBaseConfig(DocumentBaseConfigBase, AdminModel["DocumentBaseConfigEndpoint"]):
    document_type: ForeignRelation["DocumentType"] = Field(default=...)
    logo: ForeignRelation["Media"] = Field(default=...)
    sales_channels: ManyRelation["DocumentBaseConfigSalesChannel"] = Field(default=...)


class DocumentBaseConfigEndpoint(AdminEndpoint[DocumentBaseConfig]):
    name = "document_base_config"
    path = "/document-base-config"
    model_class = DocumentBaseConfig


from .document_base_config_sales_channel import DocumentBaseConfigSalesChannel  # noqa: E402
from .document_type import DocumentType  # noqa: E402
from .media import Media  # noqa: E402
