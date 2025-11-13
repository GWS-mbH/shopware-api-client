from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.media_folder import MediaFolderBase


class MediaFolder(MediaFolderBase, AdminModel["MediaFolderEndpoint"]):
    parent: ForeignRelation["MediaFolder"]
    children: ManyRelation["MediaFolder"]
    media: ManyRelation["Media"]
    default_folder: ForeignRelation["MediaDefaultFolder"]
    configuration: ForeignRelation["MediaFolderConfiguration"]


class MediaFolderEndpoint(AdminEndpoint[MediaFolder]):
    name = "media_folder"
    path = "/media-folder"
    model_class = MediaFolder


from .media import Media  # noqa: E402
from .media_default_folder import MediaDefaultFolder  # noqa: E402
from .media_folder_configuration import MediaFolderConfiguration  # noqa: E402
