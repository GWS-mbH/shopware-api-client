from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class MediaDefaultFolderBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "media_default_folder"

    entity: str
