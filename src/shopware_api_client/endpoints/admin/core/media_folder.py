from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class MediaFolderBase(ApiModelBase[EndpointClass]):
    _identifier: str = "media_folder"

    use_parent_configuration: bool | None = None
    configuration_id: IdField
    default_folder_id: IdField | None = None
    parent_id: IdField | None = None
    child_count: int | None = Field(default=None, exclude=True)
    path: str | None = Field(default=None, exclude=True)
    name: str
    custom_fields: dict[str, Any] | None = None


class MediaFolderRelations:
    parent: ForeignRelation["MediaFolder"]
    children: ManyRelation["MediaFolder"]
    media: ManyRelation["Media"]
    default_folder: ForeignRelation["MediaDefaultFolder"]
    configuration: ForeignRelation["MediaFolderConfiguration"]
    

class MediaFolder(MediaFolderBase["MediaFolderEndpoint"], MediaFolderRelations):
    pass


class MediaFolderEndpoint(EndpointBase[MediaFolder]):
    name = "media_folder"
    path = "/media-folder"
    model_class = MediaFolder


from .media import Media  # noqa: E402
from .media_default_folder import MediaDefaultFolder  # noqa: E402
from .media_folder_configuration import MediaFolderConfiguration  # noqa: E402
