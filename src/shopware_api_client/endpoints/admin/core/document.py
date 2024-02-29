from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import DocumentType, Media, Order


class DocumentBase(ApiModelBase[EndpointClass]):
    _identifier: str = "document"

    document_type_id: IdField = Field(
        ..., serialization_alias="documentTypeId", validation_alias=AliasChoices("document_type_id", "documentTypeId")
    )
    file_type: str = Field(..., serialization_alias="fileType", validation_alias=AliasChoices("file_type", "fileType"))
    referenced_document_id: IdField | None = Field(
        default=None,
        serialization_alias="referencedDocumentId",
        validation_alias=AliasChoices("referenced_document_id", "referencedDocumentId"),
    )
    order_id: IdField = Field(..., serialization_alias="orderId", validation_alias=AliasChoices("order_id", "orderId"))
    document_media_file_id: IdField | None = Field(
        default=None,
        serialization_alias="documentMediaFileId",
        validation_alias=AliasChoices("document_media_file_id", "documentMediaFileId"),
    )
    order_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderVersionId",
        validation_alias=AliasChoices("order_version_id", "orderVersionId"),
    )
    config: dict[str, Any]
    sent: bool | None = None
    static: bool | None = None
    deep_link_code: str = Field(
        ..., serialization_alias="deepLinkCode", validation_alias=AliasChoices("deep_link_code", "deepLinkCode")
    )
    document_number: str | None = Field(
        default=None,
        serialization_alias="documentNumber",
        validation_alias=AliasChoices("document_number", "documentNumber"),
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
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


class DocumentRelations:
    document_type: ClassVar[ForeignRelation["DocumentType"]] = ForeignRelation("DocumentType", "document_type_id")
    order: ClassVar[ForeignRelation["Order"]] = ForeignRelation("Order", "order_id")
    referenced_document: ClassVar[ForeignRelation["Document"]] = ForeignRelation("Document", "referenced_document_id")
    dependent_documents: ClassVar[ManyRelation["Document"]] = ManyRelation("Document", "dependentDocuments")
    document_media_file: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "document_media_file_id")


class Document(DocumentBase["DocumentEndpoint"], DocumentRelations):
    pass


class DocumentEndpoint(EndpointBase[Document]):
    name = "document"
    path = "/document"
    model_class = Document


registry.register_admin(DocumentEndpoint)
