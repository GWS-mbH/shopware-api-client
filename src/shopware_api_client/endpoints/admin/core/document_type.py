from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Document, DocumentBaseConfig, DocumentBaseConfigSalesChannel


class DocumentTypeBase(ApiModelBase[EndpointClass]):
    _identifier: str = "document_type"

    name: str
    technical_name: str = Field(
        ..., serialization_alias="technicalName", validation_alias=AliasChoices("technical_name", "technicalName")
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    translated: dict[str, Any] | None = None


class DocumentTypeRelations:
    documents: ClassVar[ManyRelation["Document"]] = ManyRelation("Document", "documents")
    document_base_configs: ClassVar[ManyRelation["DocumentBaseConfig"]] = ManyRelation(
        "DocumentBaseConfig", "documentBaseConfigs"
    )
    document_base_config_sales_channels: ClassVar[ManyRelation["DocumentBaseConfigSalesChannel"]] = ManyRelation(
        "DocumentBaseConfigSalesChannel", "documentBaseConfigSalesChannels"
    )


class DocumentType(DocumentTypeBase["DocumentTypeEndpoint"], DocumentTypeRelations):
    pass


class DocumentTypeEndpoint(EndpointBase[DocumentType]):
    name = "document_type"
    path = "/document-type"
    model_class = DocumentType


registry.register_admin(DocumentTypeEndpoint)
