from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class MediaFolderBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "media_folder"

    use_parent_configuration: bool | None = None
    configuration_id: IdField
    default_folder_id: IdField | None = None
    parent_id: IdField | None = None
    child_count: int | None = Field(default=None, exclude=True)
    path: str | None = Field(default=None, exclude=True)
    name: str
