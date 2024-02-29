from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Media


class MediaThumbnailBase(ApiModelBase[EndpointClass]):
    _identifier = "media_thumbnail"

    media_id: IdField = Field(..., serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId"))
    width: int = Field(..., exclude=True)
    height: int = Field(..., exclude=True)
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    path: str | None = Field(default=None, exclude=True)
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class MediaThumbnailRelations:
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")


class MediaThumbnail(MediaThumbnailBase["MediaThumbnailEndpoint"], MediaThumbnailRelations):
    pass


class MediaThumbnailEndpoint(EndpointBase[MediaThumbnail]):
    name = "media_thumbnail"
    path = "/media-thumbnail"
    model_class = MediaThumbnail


registry.register_admin(MediaThumbnailEndpoint)
