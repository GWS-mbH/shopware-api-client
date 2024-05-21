from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass


class MediaDefaultFolderBase(ApiModelBase[EndpointClass]):
    _identifier: str = "media_default_folder"

    entity: str
    custom_fields: dict[str, Any] | None = None
    folder: "MediaFolder | None" = None


class MediaDefaultFolderRelations:
    pass


class MediaDefaultFolder(MediaDefaultFolderBase["MediaDefaultFolderEndpoint"], MediaDefaultFolderRelations):
    pass


class MediaDefaultFolderEndpoint(EndpointBase[MediaDefaultFolder]):
    name = "media_default_folder"
    path = "/media-default-folder"
    model_class = MediaDefaultFolder


from .media_folder import MediaFolder  # noqa: E402
