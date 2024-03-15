from typing import Any

from pydantic import AliasChoices, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class DocumentBaseConfigBase(ApiModelBase[EndpointClass]):
    _identifier: str = "document_base_config"

    document_type_id: IdField
    logo_id: IdField | None = None
    name: str
    filename_prefix: str | None = None
    filename_suffix: str | None = None
    global_: bool = Field(..., serialization_alias="global", validation_alias=AliasChoices("global_", "global"))
    document_number: str | None = None
    config: dict[str, Any] | None = None
    custom_fields: dict[str, Any] | None = None


class DocumentBaseConfigRelations:
    document_type: ForeignRelation["DocumentType"]
    logo: ForeignRelation["Media"]
    sales_channels: ManyRelation["DocumentBaseConfigSalesChannel"]


class DocumentBaseConfig(DocumentBaseConfigBase["DocumentBaseConfigEndpoint"], DocumentBaseConfigRelations):
    pass


class DocumentBaseConfigEndpoint(EndpointBase[DocumentBaseConfig]):
    name = "document_base_config"
    path = "/document-base-config"
    model_class = DocumentBaseConfig


from .document_base_config_sales_channel import DocumentBaseConfigSalesChannel  # noqa: E402
from .document_type import DocumentType  # noqa: E402
from .media import Media  # noqa: E402
