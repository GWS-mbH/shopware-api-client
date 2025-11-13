from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class MediaFolderConfigurationBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "media_folder_configuration"

    create_thumbnails: bool | None = None
    keep_aspect_ration: bool | None = None
    thumbnail_quality: int | None = None
    private: bool | None = False
    no_association: bool | None = None
