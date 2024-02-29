from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField, Visibility
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import CmsBlock, CmsPage, Media


class CmsSectionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "cms_section"

    position: int
    type: str
    locked: bool | None = None
    name: str | None = None
    sizing_mode: str | None = Field(
        default=None, serialization_alias="sizingMode", validation_alias=AliasChoices("sizing_mode", "sizingMode")
    )
    mobile_behavior: str | None = Field(
        default=None,
        serialization_alias="mobileBehavior",
        validation_alias=AliasChoices("mobile_behavior", "mobileBehavior"),
    )
    background_color: str | None = Field(
        default=None,
        serialization_alias="backgroundColor",
        validation_alias=AliasChoices("background_color", "backgroundColor"),
    )
    background_media_id: IdField | None = Field(
        default=None,
        serialization_alias="backgroundMediaId",
        validation_alias=AliasChoices("background_media_id", "backgroundMediaId"),
    )
    background_media_mode: str | None = Field(
        default=None,
        serialization_alias="backgroundMediaMode",
        validation_alias=AliasChoices("background_media_mode", "backgroundMediaMode"),
    )
    css_class: str | None = Field(
        default=None, serialization_alias="cssClass", validation_alias=AliasChoices("css_class", "cssClass")
    )
    page_id: IdField = Field(..., serialization_alias="pageId", validation_alias=AliasChoices("page_id", "pageId"))
    visibility: Visibility | None = None
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    cms_page_version_id: IdField | None = Field(
        default=None,
        serialization_alias="cmsPageVersionId",
        validation_alias=AliasChoices("cms_page_version_id", "cmsPageVersionId"),
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


class CmsSectionRelations:
    page: ClassVar[ForeignRelation["CmsPage"]] = ForeignRelation("CmsPage", "page_id")
    background_media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "background_media_id")
    blocks: ClassVar[ManyRelation["CmsBlock"]] = ManyRelation("CmsBlock", "blocks")


class CmsSection(CmsSectionBase["CmsSectionEndpoint"], CmsSectionRelations):
    pass


class CmsSectionEndpoint(EndpointBase[CmsSection]):
    name = "cms_section"
    path = "/cms-section"
    model_class = CmsSection


registry.register_admin(CmsSectionEndpoint)
