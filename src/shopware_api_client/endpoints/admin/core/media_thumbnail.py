from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class MediaThumbnailBase(ApiModelBase[EndpointClass]):
    _identifier = "media_thumbnail"

    media_id: IdField
    width: int = Field(default=0, exclude=True)
    height: int = Field(default=0, exclude=True)
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    path: str | None = Field(default=None, exclude=True)
    custom_fields: dict[str, Any] | None = None


class MediaThumbnailRelations:
    media: ForeignRelation["Media"]


class MediaThumbnail(MediaThumbnailBase["MediaThumbnailEndpoint"], MediaThumbnailRelations):
    pass


class MediaThumbnailEndpoint(EndpointBase[MediaThumbnail]):
    name = "media_thumbnail"
    path = "/media-thumbnail"
    model_class = MediaThumbnail


from .media import Media  # noqa: E402
