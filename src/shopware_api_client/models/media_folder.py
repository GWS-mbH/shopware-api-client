from typing import Annotated

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class MediaFolderBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "media_folder"

    use_parent_configuration: bool | None = None
    configuration_id: Annotated[IdField, RefersTo("media_folder_configuration")]
    default_folder_id: Annotated[IdField | None, RefersTo("media_default_folder")] = None
    parent_id: Annotated[IdField | None, RefersTo("media_folder")] = None
    child_count: int | None = Field(default=None, exclude=True)
    path: str | None = Field(default=None, exclude=True)
    name: str
