from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class MediaThumbnailSizeBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "media_thumbnail_size"

    width: int
    height: int
