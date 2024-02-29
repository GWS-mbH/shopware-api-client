from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import DocumentBaseConfigSalesChannel, DocumentType, Media


class DocumentBaseConfigBase(ApiModelBase[EndpointClass]):
    _identifier: str = "document_base_config"

    document_type_id: IdField = Field(
        ..., serialization_alias="documentTypeId", validation_alias=AliasChoices("document_type_id", "documentTypeId")
    )
    logo_id: IdField | None = Field(
        default=None, serialization_alias="logoId", validation_alias=AliasChoices("logo_id", "logoId")
    )
    name: str
    filename_prefix: str | None = Field(
        default=None,
        serialization_alias="filenamePrefix",
        validation_alias=AliasChoices("filename_prefix", "filenamePrefix"),
    )
    filename_suffix: str | None = Field(
        default=None,
        serialization_alias="filenameSuffix",
        validation_alias=AliasChoices("filename_suffix", "filenameSuffix"),
    )
    global_: bool = Field(..., serialization_alias="global", validation_alias=AliasChoices("global_", "global"))
    document_number: str | None = Field(
        default=None,
        serialization_alias="documentNumber",
        validation_alias=AliasChoices("document_number", "documentNumber"),
    )
    config: dict[str, Any] | None = None
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class DocumentBaseConfigRelations:
    document_type: ClassVar[ForeignRelation["DocumentType"]] = ForeignRelation("DocumentType", "document_type_id")
    logo: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "logo_id")
    sales_channels: ClassVar[ManyRelation["DocumentBaseConfigSalesChannel"]] = ManyRelation(
        "DocumentBaseConfigSalesChannel", "salesChannels"
    )


class DocumentBaseConfig(DocumentBaseConfigBase["DocumentBaseConfigEndpoint"], DocumentBaseConfigRelations):
    pass


class DocumentBaseConfigEndpoint(EndpointBase[DocumentBaseConfig]):
    name = "document_base_config"
    path = "/document-base-config"
    model_class = DocumentBaseConfig


registry.register_admin(DocumentBaseConfigEndpoint)
