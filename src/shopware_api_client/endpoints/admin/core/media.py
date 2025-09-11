from typing import Any

from pydantic import AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class MediaBase(ApiModelBase[EndpointClass]):
    _identifier: str = "media"

    user_id: IdField | None = None
    media_folder_id: IdField | None = Field(default=None)
    mime_type: str | None = Field(default=None)
    file_extension: str | None = Field(default=None)
    uploaded_at: AwareDatetime | None = Field(default=None, exclude=True)
    file_name: str | None = Field(default=None)
    file_size: int | None = Field(default=None, exclude=True)
    meta_data: dict[str, Any] | None = Field(default=None, exclude=True)
    media_type: dict[str, Any] | None = Field(default=None, exclude=True)
    config: dict[str, Any] | None = Field(default=None, exclude=True)
    alt: str | None = None
    title: str | None = None
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    path: str | None = Field(default=None)
    has_file: bool | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    private: bool | None = False
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class MediaRelations:
    tags: ManyRelation["Tag"]
    thumbnails: ManyRelation["MediaThumbnail"]
    user: ForeignRelation["User"]
    categories: ManyRelation["Category"]
    product_manufacturers: ManyRelation["ProductManufacturer"]
    product_media: ManyRelation["ProductMedia"]
    product_downloads: ManyRelation["ProductDownload"]
    order_line_item_downloads: ManyRelation["OrderLineItemDownload"]
    avatar_users: ManyRelation["Media"]
    media_folder: ForeignRelation["MediaFolder"]
    property_group_options: ManyRelation["PropertyGroupOption"]
    document_base_configs: ManyRelation["DocumentBaseConfig"]
    shipping_methods: ManyRelation["ShippingMethod"]
    payment_methods: ManyRelation["PaymentMethod"]
    product_configurator_settings: ManyRelation["ProductConfiguratorSetting"]
    order_line_items: ManyRelation["OrderLineItem"]
    cms_blocks: ManyRelation["CmsBlock"]
    cms_sections: ManyRelation["CmsSection"]
    cms_pages: ManyRelation["CmsPage"]
    documents: ManyRelation["Document"]

    """
    Todo:
    mail_template_media[MailTemplateMedia], app_payment_methods[AppPaymentMethod],
    app_shipping_methods[AppShippingMethod]
    """


class Media(MediaBase["MediaEndpoint"], MediaRelations):
    async def upload_file(self, file_extension: str = "jpg", file_name: str | None = None, url: str | None = None, file: bytes | None = None) -> bool:
        assert self.id is not None
        return await self._get_endpoint().upload(self.id, file_extension=file_extension, file_name=file_name, url=url, file=file)
    

class MediaEndpoint(EndpointBase[Media]):
    name = "media"
    path = "/media"
    model_class = Media

    async def upload(self, pk: str, file_extension: str = "jpg", file_name: str | None = None, 
                     url: str | None = None, file: bytes | None = None, **request_kwargs: Any) -> bool:
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
