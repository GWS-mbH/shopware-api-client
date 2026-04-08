from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.media_folder_configuration import MediaFolderConfigurationBase


class MediaFolderConfiguration(MediaFolderConfigurationBase, AdminModel["MediaFolderConfigurationEndpoint"]):
    media_folders: ManyRelation["MediaFolder"] = Field(default=...)
    media_thumbnail_sizes: ManyRelation["MediaThumbnailSize"] = Field(default=...)


class MediaFolderConfigurationEndpoint(AdminEndpoint[MediaFolderConfiguration]):
    name = "media_folder_configuration"
    path = "/media-folder-configuration"
    model_class = MediaFolderConfiguration


from .media_folder import MediaFolder  # noqa: E402
from .media_thumbnail_size import MediaThumbnailSize  # noqa: E402
