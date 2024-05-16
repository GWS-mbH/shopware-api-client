from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class MediaFolderConfigurationBase(ApiModelBase[EndpointClass]):
    _identifier: str = "media_folder_configuration"

    create_thumbnails: bool | None = None
    keep_aspect_ration: bool | None = None
    thumbnail_quality: int | None = None
    private: bool | None = False
    no_association: bool | None = None
    custom_fields: dict[str, Any] | None = None


class MediaFolderConfigurationRelations:
    media_folders: ManyRelation["MediaFolder"]
    media_thumbnail_sizes: ManyRelation["MediaThumbnailSize"]


class MediaFolderConfiguration(MediaFolderConfigurationBase["MediaFolderConfigurationEndpoint"], MediaFolderConfigurationRelations):
    pass


class MediaFolderConfigurationEndpoint(EndpointBase[MediaFolderConfiguration]):
    name = "media_folder_configuration"
    path = "/media-folder-configuration"
    model_class = MediaFolderConfiguration


from .media_folder import MediaFolder  # noqa: E402
from .media_thumbnail_size import MediaThumbnailSize  # noqa: E402
