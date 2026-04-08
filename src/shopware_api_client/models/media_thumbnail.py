from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class MediaThumbnailBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "media_thumbnail"

    media_id: IdField
    media_thumbnail_size_id: IdField | None = None  # Will get required with 6.8.0
    width: int = Field(default=0, exclude=True)
    height: int = Field(default=0, exclude=True)
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    path: str | None = None
