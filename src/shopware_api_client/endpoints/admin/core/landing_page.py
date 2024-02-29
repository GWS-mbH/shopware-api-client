from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import CmsPage, SalesChannel, SeoUrl, Tag


class LandingPageBase(ApiModelBase[EndpointClass]):
    _identifier: str = "landing_page"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    active: bool | None = None
    name: str
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    slot_config: dict[str, Any] | None = Field(
        default=None, serialization_alias="slotConfig", validation_alias=AliasChoices("slot_config", "slotConfig")
    )
    meta_title: str | None = Field(
        default=None, serialization_alias="metaTitle", validation_alias=AliasChoices("meta_title", "metaTitle")
    )
    meta_description: str | None = Field(
        default=None,
        serialization_alias="metaDescription",
        validation_alias=AliasChoices("meta_description", "metaDescription"),
    )
    keywords: str | None = None
    url: str
    cms_page_id: IdField | None = Field(
        default=None, serialization_alias="cmsPageId", validation_alias=AliasChoices("cms_page_id", "cmsPageId")
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
    translated: dict[str, Any] | None = None


class LandingPageRelations:
    tags: ClassVar[ManyRelation["Tag"]] = ManyRelation("Tag", "tags")
    cms_page: ClassVar[ForeignRelation["CmsPage"]] = ForeignRelation("CmsPage", "cms_page_id")
    sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "salesChannels")
    seo_urls: ClassVar[ManyRelation["SeoUrl"]] = ManyRelation("SeoUrl", "seoUrls")


class LandingPage(LandingPageBase["LandingPageEndpoint"], LandingPageRelations):
    pass


class LandingPageEndpoint(EndpointBase[LandingPage]):
    name = "landing_page"
    path = "/landing-page"
    model_class = LandingPage


registry.register_admin(LandingPageEndpoint)
