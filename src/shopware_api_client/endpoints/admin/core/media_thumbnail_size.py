from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class MediaThumbnailSizeBase(ApiModelBase[EndpointClass]):
    _identifier: str = "media_thumbnail_size"

    width: int
    height: int
    custom_fields: dict[str, Any] | None = None


class MediaThumbnailSizeRelations:
    media_folder_configurations: ManyRelation["MediaFolderConfiguration"]


class MediaThumbnailSize(MediaThumbnailSizeBase["MediaThumbnailSizeEndpoint"], MediaThumbnailSizeRelations):
    pass


class MediaThumbnailSizeEndpoint(EndpointBase[MediaThumbnailSize]):
    name = "media_thumbnail_size"
    path = "/media-thumbnail-size"
    model_class = MediaThumbnailSize


from .media_folder_configuration import MediaFolderConfiguration  # noqa: E402
