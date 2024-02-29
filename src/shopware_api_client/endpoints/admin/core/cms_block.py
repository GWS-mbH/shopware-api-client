from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField, Visibility
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import CmsSection, CmsSlot, Media


class CmsBlockBase(ApiModelBase[EndpointClass]):
    _identifier: str = "cms_block"

    position: int
    type: str
    locked: bool | None = None
    name: str | None = None
    section_position: str | None = Field(
        default=None,
        serialization_alias="sectionPosition",
        validation_alias=AliasChoices("section_position", "sectionPosition"),
    )
    margin_top: str | None = Field(
        default=None, serialization_alias="marginTop", validation_alias=AliasChoices("margin_top", "marginTop")
    )
    margin_bottom: str | None = Field(
        default=None, serialization_alias="marginBottom", validation_alias=AliasChoices("margin_bottom", "marginBottom")
    )
    margin_left: str | None = Field(
        default=None, serialization_alias="marginLeft", validation_alias=AliasChoices("margin_left", "marginLeft")
    )
    margin_right: str | None = Field(
        default=None, serialization_alias="marginRight", validation_alias=AliasChoices("margin_right", "marginRight")
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
    visibility: Visibility | None = None
    section_id: IdField = Field(
        ..., serialization_alias="sectionId", validation_alias=AliasChoices("section_id", "sectionId")
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    cms_section_version_id: IdField | None = Field(
        default=None,
        serialization_alias="cmsSectionVersionId",
        validation_alias=AliasChoices("cms_section_version_id", "cmsSectionVersionId"),
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


class CmsBlockRelations:
    section: ClassVar[ForeignRelation["CmsSection"]] = ForeignRelation("CmsSection", "section_id")
    background_media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "background_media_id")
    slots: ClassVar[ManyRelation["CmsSlot"]] = ManyRelation("CmsSlot", "slots")


class CmsBlock(CmsBlockBase["CmsBlockEndpoint"], CmsBlockRelations):
    pass


class CmsBlockEndpoint(EndpointBase[CmsBlock]):
    name = "cms_block"
    path = "/cms-block"
    model_class = CmsBlock


registry.register_admin(CmsBlockEndpoint)
