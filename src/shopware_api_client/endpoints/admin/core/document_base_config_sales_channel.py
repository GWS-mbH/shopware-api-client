from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class DocumentBaseConfigSalesChannelBase(ApiModelBase[EndpointClass]):
    _identifier: str = "document_base_config_sales_channel"

    document_base_config_id: IdField
    sales_channel_id: IdField | None = None
    document_type_id: IdField | None = None


class DocumentBaseConfigSalesChannelRelations:
    document_type: ForeignRelation["DocumentType"]
    document_base_config: ForeignRelation["DocumentBaseConfig"]
    sales_channel: ForeignRelation["SalesChannel"]


class DocumentBaseConfigSalesChannel(
    DocumentBaseConfigSalesChannelBase["DocumentBaseConfigSalesChannelEndpoint"],
    DocumentBaseConfigSalesChannelRelations,
):
    pass


class DocumentBaseConfigSalesChannelEndpoint(EndpointBase[DocumentBaseConfigSalesChannel]):
    name = "document_base_config_sales_channel"
    path = "/document-base-config-sales-channel"
    model_class = DocumentBaseConfigSalesChannel


from .document_base_config import DocumentBaseConfig  # noqa: E402
from .document_type import DocumentType  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
