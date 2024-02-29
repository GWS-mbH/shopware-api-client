from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import DocumentBaseConfig, DocumentType, SalesChannel


class DocumentBaseConfigSalesChannelBase(ApiModelBase[EndpointClass]):
    _identifier: str = "document_base_config_sales_channel"

    document_base_config_id: IdField = Field(
        ...,
        serialization_alias="documentBaseConfigId",
        validation_alias=AliasChoices("document_base_config_id", "documentBaseConfigId"),
    )
    sales_channel_id: IdField | None = Field(
        default=None,
        serialization_alias="salesChannelId",
        validation_alias=AliasChoices("sales_channel_id", "salesChannelId"),
    )
    document_type_id: IdField | None = Field(
        default=None,
        serialization_alias="documentTypeId",
        validation_alias=AliasChoices("document_type_id", "documentTypeId"),
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


class DocumentBaseConfigSalesChannelRelations:
    document_type: ClassVar[ForeignRelation["DocumentType"]] = ForeignRelation("DocumentType", "document_type_id")
    document_base_config: ClassVar[ForeignRelation["DocumentBaseConfig"]] = ForeignRelation(
        "DocumentBaseConfig", "document_base_config_id"
    )
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")


class DocumentBaseConfigSalesChannel(
    DocumentBaseConfigSalesChannelBase["DocumentBaseConfigSalesChannelEndpoint"],
    DocumentBaseConfigSalesChannelRelations,
):
    pass


class DocumentBaseConfigSalesChannelEndpoint(EndpointBase[DocumentBaseConfigSalesChannel]):
    name = "document_base_config_sales_channel"
    path = "/document-base-config-sales-channel"
    model_class = DocumentBaseConfigSalesChannel


registry.register_admin(DocumentBaseConfigSalesChannelEndpoint)
