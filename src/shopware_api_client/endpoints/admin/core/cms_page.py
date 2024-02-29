from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Category, CmsSection, LandingPage, Media, Product, SalesChannel


class CmsPageBase(ApiModelBase[EndpointClass]):
    _identifier: str = "cms_page"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    name: str | None = None
    type: str
    entity: str | None = None
    css_class: str | None = Field(
        default=None, serialization_alias="cssClass", validation_alias=AliasChoices("css_class", "cssClass")
    )
    config: dict[str, Any] | None = None
    preview_media_id: IdField | None = Field(
        default=None,
        serialization_alias="previewMediaId",
        validation_alias=AliasChoices("preview_media_id", "previewMediaId"),
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    locked: bool | None = None
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


class CmsPageRelations:
    sections: ClassVar[ManyRelation["CmsSection"]] = ManyRelation("CmsSection", "sections")
    preview_media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "preview_media_id")
    categories: ClassVar[ManyRelation["Category"]] = ManyRelation("Category", "categories")
    landing_pages: ClassVar[ManyRelation["LandingPage"]] = ManyRelation("LandingPage", "landingPages")
    home_sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "homeSalesChannels")
    products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "products")


class CmsPage(CmsPageBase["CmsPageEndpoint"], CmsPageRelations):
    pass


class CmsPageEndpoint(EndpointBase[CmsPage]):
    name = "cms_page"
    path = "/cms-page"
    model_class = CmsPage


registry.register_admin(CmsPageEndpoint)
