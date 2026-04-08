from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.media_thumbnail import MediaThumbnailBase


class MediaThumbnail(MediaThumbnailBase, AdminModel["MediaThumbnailEndpoint"]):
    media: ForeignRelation["Media"] = Field(default=...)


class MediaThumbnailEndpoint(AdminEndpoint[MediaThumbnail]):
    name = "media_thumbnail"
    path = "/media-thumbnail"
    model_class = MediaThumbnail


from .media import Media  # noqa: E402
