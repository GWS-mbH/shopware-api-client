from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.models.media_default_folder import MediaDefaultFolderBase


class MediaDefaultFolder(MediaDefaultFolderBase, AdminModel["MediaDefaultFolderEndpoint"]):
    folder: "MediaFolder | None" = None


class MediaDefaultFolderEndpoint(AdminEndpoint[MediaDefaultFolder]):
    name = "media_default_folder"
    path = "/media-default-folder"
    model_class = MediaDefaultFolder


from .media_folder import MediaFolder  # noqa: E402
