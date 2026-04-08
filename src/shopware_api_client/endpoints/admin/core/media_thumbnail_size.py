from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.media_thumbnail_size import MediaThumbnailSizeBase


class MediaThumbnailSize(MediaThumbnailSizeBase, AdminModel["MediaThumbnailSizeEndpoint"]):
    media_folder_configurations: ManyRelation["MediaFolderConfiguration"] = Field(default=...)
    media_thumbnails: ManyRelation["MediaThumbnail"] = Field(default=...)


class MediaThumbnailSizeEndpoint(AdminEndpoint[MediaThumbnailSize]):
    name = "media_thumbnail_size"
    path = "/media-thumbnail-size"
    model_class = MediaThumbnailSize


from .media_folder_configuration import MediaFolderConfiguration  # noqa: E402
from .media_thumbnail import MediaThumbnail  # noqa: E402
