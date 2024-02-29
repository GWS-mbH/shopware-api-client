from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import (
        Category,
        CmsBlock,
        CmsPage,
        CmsSection,
        Document,
        DocumentBaseConfig,
        MediaThumbnail,
        OrderLineItem,
        OrderLineItemDownload,
        PaymentMethod,
        ProductConfiguratorSetting,
        ProductDownload,
        PropertyGroupOption,
        ShippingMethod,
        Tag,
        User,
    )


class MediaBase(ApiModelBase[EndpointClass]):
    _identifier: str = "media"

    user_id: IdField | None = Field(
        default=None, serialization_alias="userId", validation_alias=AliasChoices("user_id", "userId")
    )
    media_folder_id: IdField | None = Field(
        default=None,
        serialization_alias="mediaFolderId",
        validation_alias=AliasChoices("media_folder_id", "mediaFolderId"),
        exclude=True,
    )
    mime_type: str | None = Field(
        default=None,
        serialization_alias="mimeType",
        validation_alias=AliasChoices("mime_type", "mimeType"),
        exclude=True,
    )
    file_extension: str | None = Field(
        default=None,
        serialization_alias="fileExtension",
        validation_alias=AliasChoices("file_extension", "fileExtension"),
        exclude=True,
    )
    uploaded_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="uploadedAt",
        validation_alias=AliasChoices("uploaded_at", "uploadedAt"),
        exclude=True,
    )
    file_name: str | None = Field(
        default=None,
        serialization_alias="fileName",
        validation_alias=AliasChoices("file_name", "fileName"),
        exclude=True,
    )
    file_size: int | None = Field(
        default=None,
        serialization_alias="fileSize",
        validation_alias=AliasChoices("file_size", "fileSize"),
        exclude=True,
    )
    meta_data: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="metaData",
        validation_alias=AliasChoices("meta_data", "metaData"),
        exclude=True,
    )
    media_type: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="mediaType",
        validation_alias=AliasChoices("media_type", "mediaType"),
        exclude=True,
    )
    config: dict[str, Any] | None = Field(default=None, exclude=True)
    alt: str | None = None
    title: str | None = None
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    path: str | None = Field(default=None, exclude=True)
    has_file: bool | None = Field(
        None,
        alias="hasFile",
        description="Runtime field, cannot be used as part of the criteria.",
    )
    private: bool | None = None
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
    translated: dict[str, Any] | None = None


class MediaRelations:
    tags: ClassVar[ManyRelation["Tag"]] = ManyRelation("Tag", "tags")
    thumbnails: ClassVar[ManyRelation["MediaThumbnail"]] = ManyRelation("MediaThumbnail", "thumbnails")
    user: ClassVar[ForeignRelation["User"]] = ForeignRelation("User", "user_id")
    categories: ClassVar[ManyRelation["Category"]] = ManyRelation("Category", "categories")
    product_downloads: ClassVar[ManyRelation["ProductDownload"]] = ManyRelation("ProductDownload", "productDownloads")
    order_line_item_downloads: ClassVar[ManyRelation["OrderLineItemDownload"]] = ManyRelation(
        "OrderLineItemDownload", "orderLineItemDownloads"
    )
    avatar_users: ClassVar[ManyRelation["Media"]] = ManyRelation("Media", "avatarUsers")
    property_group_options: ClassVar[ManyRelation["PropertyGroupOption"]] = ManyRelation(
        "PropertyGroupOption", "propertyGroupOptions"
    )
    document_base_configs: ClassVar[ManyRelation["DocumentBaseConfig"]] = ManyRelation(
        "DocumentBaseConfig", "documentBaseConfigs"
    )
    shipping_methods: ClassVar[ManyRelation["ShippingMethod"]] = ManyRelation("ShippingMethod", "shippingMethods")
    payment_methods: ClassVar[ManyRelation["PaymentMethod"]] = ManyRelation("PaymentMethod", "payment-methods")
    product_configurator_settings: ClassVar[ManyRelation["ProductConfiguratorSetting"]] = ManyRelation(
        "ProductConfiguratorSetting", "productConfiguratorSettings"
    )
    order_line_items: ClassVar[ManyRelation["OrderLineItem"]] = ManyRelation("OrderLineItem", "orderLineItems")
    cms_blocks: ClassVar[ManyRelation["CmsBlock"]] = ManyRelation("CmsBlock", "cmsBlocks")
    cms_sections: ClassVar[ManyRelation["CmsSection"]] = ManyRelation("CmsSection", "cmsSections")
    cms_pages: ClassVar[ManyRelation["CmsPage"]] = ManyRelation("CmsPage", "cmsPages")
    documents: ClassVar[ManyRelation["Document"]] = ManyRelation("Document", "documents")

    """
    Todo:
    product_manufacturer[ProductManufacturer], product_media[ProductMedia],
    media_folder[MediaFolder], mail_template_media[MailTemplateMedia], app_payment_methods[AppPaymentMethod],
    app_shipping_methods[AppShippingMethod]
    """


class Media(MediaBase["MediaEndpoint"], MediaRelations):
    pass


class MediaEndpoint(EndpointBase[Media]):
    name = "media"
    path = "/media"
    model_class = Media


registry.register_admin(MediaEndpoint)
