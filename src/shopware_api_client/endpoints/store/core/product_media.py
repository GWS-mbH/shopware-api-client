from shopware_api_client.models.product_media import ProductMediaBase


class ProductMedia(ProductMediaBase):
    media: "Media | None" = None
    thumbnails: list["MediaThumbnail"] | None = None


from .media import Media  # noqa: E402
from .media_thumbnail import MediaThumbnail  # noqa: E402
