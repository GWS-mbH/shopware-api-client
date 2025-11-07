from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.document_base_config_sales_channel import (
    DocumentBaseConfigSalesChannel as DocumentBaseConfigSalesChannelBase,
)


class DocumentBaseConfigSalesChannel(
    DocumentBaseConfigSalesChannelBase, AdminModel["DocumentBaseConfigSalesChannelEndpoint"]
):
    document_type: ForeignRelation["DocumentType"]
    document_base_config: ForeignRelation["DocumentBaseConfig"]
    sales_channel: ForeignRelation["SalesChannel"]


class DocumentBaseConfigSalesChannelEndpoint(AdminEndpoint[DocumentBaseConfigSalesChannel]):
    name = "document_base_config_sales_channel"
    path = "/document-base-config-sales-channel"
    model_class = DocumentBaseConfigSalesChannel


from .document_base_config import DocumentBaseConfig  # noqa: E402
from .document_type import DocumentType  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
