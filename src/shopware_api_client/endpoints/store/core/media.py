from shopware_api_client.models.media import MediaBase


class Media(MediaBase):
    thumbnails: list["MediaThumbnail"] | None = None


from .media_thumbnail import MediaThumbnail  # noqa: E402
