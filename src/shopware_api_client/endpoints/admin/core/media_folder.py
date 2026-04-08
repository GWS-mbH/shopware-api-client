from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.media_folder import MediaFolderBase


class MediaFolder(MediaFolderBase, AdminModel["MediaFolderEndpoint"]):
    parent: ForeignRelation["MediaFolder"] = Field(default=...)
    children: ManyRelation["MediaFolder"] = Field(default=...)
    media: ManyRelation["Media"] = Field(default=...)
    default_folder: ForeignRelation["MediaDefaultFolder"] = Field(default=...)
    configuration: ForeignRelation["MediaFolderConfiguration"] = Field(default=...)


class MediaFolderEndpoint(AdminEndpoint[MediaFolder]):
    name = "media_folder"
    path = "/media-folder"
    model_class = MediaFolder


from .media import Media  # noqa: E402
from .media_default_folder import MediaDefaultFolder  # noqa: E402
from .media_folder_configuration import MediaFolderConfiguration  # noqa: E402
