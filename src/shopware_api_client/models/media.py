from typing import Any
from pydantic import Field, AwareDatetime

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class MediaBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "media"

    user_id: IdField | None = None
    media_folder_id: IdField | None = Field(default=None)
    mime_type: str | None = Field(default=None)
    file_extension: str | None = Field(default=None)
    uploaded_at: AwareDatetime | None = Field(default=None, exclude=True)
    file_name: str | None = Field(default=None)
    file_size: int | None = Field(default=None, exclude=True)
    meta_data: dict[str, Any] | None = Field(default=None, exclude=True)
    media_type: dict[str, Any] | None = Field(default=None, exclude=True)
    config: dict[str, Any] | None = Field(default=None, exclude=True)
    alt: str | None = None
    title: str | None = None
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    path: str | None = Field(default=None)
    has_file: bool | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    private: bool | None = False
