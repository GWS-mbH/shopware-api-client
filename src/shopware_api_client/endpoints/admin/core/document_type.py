from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class DocumentTypeBase(ApiModelBase[EndpointClass]):
    _identifier: str = "document_type"

    name: str
    technical_name: str
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class DocumentTypeRelations:
    documents: ManyRelation["Document"]
    document_base_configs: ManyRelation["DocumentBaseConfig"]
    document_base_config_sales_channels: ManyRelation["DocumentBaseConfigSalesChannel"]


class DocumentType(DocumentTypeBase["DocumentTypeEndpoint"], DocumentTypeRelations):
    pass


class DocumentTypeEndpoint(EndpointBase[DocumentType]):
    name = "document_type"
    path = "/document-type"
    model_class = DocumentType


from .document import Document  # noqa: E402
from .document_base_config import DocumentBaseConfig  # noqa: E402
from .document_base_config_sales_channel import DocumentBaseConfigSalesChannel  # noqa: E402
