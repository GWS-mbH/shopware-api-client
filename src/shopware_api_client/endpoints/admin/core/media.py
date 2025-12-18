from typing import Any

from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.media import MediaBase


class Media(MediaBase, AdminModel["MediaEndpoint"]):
    tags: ManyRelation["Tag"] = Field(default=...)
    thumbnails: ManyRelation["MediaThumbnail"] = Field(default=...)
    user: ForeignRelation["User"] = Field(default=...)
    categories: ManyRelation["Category"] = Field(default=...)
    product_manufacturers: ManyRelation["ProductManufacturer"] = Field(default=...)
    product_media: ManyRelation["ProductMedia"] = Field(default=...)
    product_downloads: ManyRelation["ProductDownload"] = Field(default=...)
    order_line_item_downloads: ManyRelation["OrderLineItemDownload"] = Field(default=...)
    avatar_users: ManyRelation["Media"] = Field(default=...)
    media_folder: ForeignRelation["MediaFolder"] = Field(default=...)
    property_group_options: ManyRelation["PropertyGroupOption"] = Field(default=...)
    document_base_configs: ManyRelation["DocumentBaseConfig"] = Field(default=...)
    shipping_methods: ManyRelation["ShippingMethod"] = Field(default=...)
    payment_methods: ManyRelation["PaymentMethod"] = Field(default=...)
    product_configurator_settings: ManyRelation["ProductConfiguratorSetting"] = Field(default=...)
    order_line_items: ManyRelation["OrderLineItem"] = Field(default=...)
    cms_blocks: ManyRelation["CmsBlock"] = Field(default=...)
    cms_sections: ManyRelation["CmsSection"] = Field(default=...)
    cms_pages: ManyRelation["CmsPage"] = Field(default=...)
    documents: ManyRelation["Document"] = Field(default=...)

    """
    Todo:
    mail_template_media[MailTemplateMedia], app_payment_methods[AppPaymentMethod],
    app_shipping_methods[AppShippingMethod]
    """

    async def upload_file(
        self,
        file_extension: str = "jpg",
        file_name: str | None = None,
        url: str | None = None,
        file: bytes | None = None,
    ) -> bool:
        assert self.id is not None
        return await self._get_endpoint().upload(
            self.id, file_extension=file_extension, file_name=file_name, url=url, file=file
        )


class MediaEndpoint(AdminEndpoint[Media]):
    name = "media"
    path = "/media"
    model_class = Media

    async def upload(
        self,
        pk: str,
        file_extension: str = "jpg",
        file_name: str | None = None,
        url: str | None = None,
        file: bytes | None = None,
        **request_kwargs: Any,
    ) -> bool:
        api_url = f"/_action/media/{pk}/upload?extension={file_extension}"

        if file_name is not None:
            api_url += f"&fileName={file_name}"

        if url is not None:
            response = await self.client.post(api_url, json={"url": url}, **request_kwargs)
        elif file is not None:
            response = await self.client.upload(api_url, data=file, **request_kwargs)
        else:
            raise ValueError("Either url or file must be provided.")

        if response.status_code == 204:
            return True
        return False


from .category import Category  # noqa: E402
from .cms_block import CmsBlock  # noqa: E402
from .cms_page import CmsPage  # noqa: E402
from .cms_section import CmsSection  # noqa: E402
from .document import Document  # noqa: E402
from .document_base_config import DocumentBaseConfig  # noqa: E402
from .media_folder import MediaFolder  # noqa: E402
from .media_thumbnail import MediaThumbnail  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
from .order_line_item_download import OrderLineItemDownload  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .product_configurator_setting import ProductConfiguratorSetting  # noqa: E402
from .product_download import ProductDownload  # noqa: E402
from .product_manufacturer import ProductManufacturer  # noqa: E402
from .product_media import ProductMedia  # noqa: E402
from .property_group_option import PropertyGroupOption  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
from .tag import Tag  # noqa: E402
from .user import User  # noqa: E402
