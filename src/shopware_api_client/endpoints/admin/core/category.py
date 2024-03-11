from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import CmsPage, MainCategory, Media, Product, ProductStream, SalesChannel, SeoUrl, Tag


class CategoryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "category"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    parent_id: IdField | None = Field(
        default=None, serialization_alias="parentId", validation_alias=AliasChoices("parent_id", "parentId")
    )
    parent_version_id: IdField | None = Field(
        default=None,
        serialization_alias="parentVersionId",
        validation_alias=AliasChoices("parent_version_id", "parentVersionId"),
    )
    after_category_id: IdField | None = Field(
        default=None,
        serialization_alias="afterCategoryId",
        validation_alias=AliasChoices("after_category_id", "afterCategoryId"),
    )
    after_category_version_id: IdField | None = Field(
        default=None,
        serialization_alias="afterCategoryVersionId",
        validation_alias=AliasChoices("after_category_version_id", "afterCategoryVersionId"),
    )
    media_id: IdField | None = Field(
        default=None, serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId")
    )
    display_nested_products: bool = Field(
        ...,
        serialization_alias="displayNestedProducts",
        validation_alias=AliasChoices("display_nested_products", "displayNestedProducts"),
    )
    auto_increment: int | None = Field(
        default=None,
        serialization_alias="autoIncrement",
        validation_alias=AliasChoices("auto_increment", "autoIncrement"),
        exclude=True,
    )
    breadcrumb: list[str] | None = Field(default=None, exclude=True)
    level: int | None = Field(default=None, exclude=True)
    path: str | None = Field(default=None, exclude=True)
    child_count: int | None = Field(
        default=None,
        serialization_alias="childCount",
        validation_alias=AliasChoices("child_count", "childCount"),
        exclude=True,
    )
    type: str
    product_assignment_type: str = Field(
        ...,
        serialization_alias="productAssignmentType",
        validation_alias=AliasChoices("product_assignment_type", "productAssignmentType"),
    )
    visible: bool | None = None
    active: bool | None = None
    cms_page_id_sIdFieldched: bool | None = Field(
        default=None,
        alias="cmsPageIdSwitched",
        description="Runtime field, cannot be used as part of the criteria.",
    )
    visible_child_count: int | None = Field(
        default=None,
        alias="visibleChildCount",
        description="Runtime field, cannot be used as part of the criteria.",
    )
    name: str
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    slot_config: dict[str, Any] | None = Field(
        default=None, serialization_alias="slotConfig", validation_alias=AliasChoices("slot_config", "slotConfig")
    )
    link_type: str | None = Field(
        default=None, serialization_alias="linkType", validation_alias=AliasChoices("link_type", "linkType")
    )
    internal_link: str | None = Field(
        default=None, serialization_alias="internalLink", validation_alias=AliasChoices("internal_link", "internalLink")
    )
    external_link: str | None = Field(
        default=None, serialization_alias="externalLink", validation_alias=AliasChoices("external_link", "externalLink")
    )
    link_new_tab: bool | None = Field(
        default=None, serialization_alias="linkNewTab", validation_alias=AliasChoices("link_new_tab", "linkNewTab")
    )
    description: str | None = None
    meta_title: str | None = Field(
        default=None, serialization_alias="metaTitle", validation_alias=AliasChoices("meta_title", "metaTitle")
    )
    meta_description: str | None = Field(
        default=None,
        serialization_alias="metaDescription",
        validation_alias=AliasChoices("meta_description", "metaDescription"),
    )
    keywords: str | None = None
    cms_page_id: IdField | None = Field(
        default=None, serialization_alias="cmsPageId", validation_alias=AliasChoices("cms_page_id", "cmsPageId")
    )
    cms_page_version_id: IdField | None = Field(
        default=None,
        serialization_alias="cmsPageVersionId",
        validation_alias=AliasChoices("cms_page_version_id", "cmsPageVersionId"),
    )
    product_stream_id: IdField | None = Field(
        default=None,
        serialization_alias="productStreamId",
        validation_alias=AliasChoices("product_stream_id", "productStreamId"),
    )
    custom_entity_type_id: IdField | None = Field(
        default=None,
        serialization_alias="customEntityTypeId",
        validation_alias=AliasChoices("custom_entity_type_id", "customEntityTypeId"),
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


class CategoryRelations:
    parent: ClassVar[ForeignRelation["Category"]] = ForeignRelation("Category", "parent_id")
    children: ClassVar[ManyRelation["Category"]] = ManyRelation("Category", "children")
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")
    products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "products")
    nested_products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "nestedProducts")
    tags: ClassVar[ManyRelation["Tag"]] = ManyRelation("Tag", "tags")
    cms_page: ClassVar[ForeignRelation["CmsPage"]] = ForeignRelation("CmsPage", "cms_page_id")
    product_stream: ClassVar[ForeignRelation["ProductStream"]] = ForeignRelation("ProductStream", "product_stream_id")
    navigation_sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "navigationSalesChannels"
    )
    footer_sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "footerSalesChannels")
    service_sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "serviceSalesChannels"
    )
    main_categories: ClassVar[ManyRelation["MainCategory"]] = ManyRelation("MainCategory", "mainCategories")
    seo_urls: ClassVar[ManyRelation["SeoUrl"]] = ManyRelation("SeoUrl", "seoUrls")


class Category(CategoryBase["CategoryEndpoint"], CategoryRelations):
    pass


class CategoryEndpoint(EndpointBase[Category]):
    name = "category"
    path = "/category"
    model_class = Category


registry.register_admin(CategoryEndpoint)
