from shopware_api_client.models.cms_block import CmsBlockBase


class CmsBlock(CmsBlockBase):
    background_media: "Media | None" = None
    slots: list["CmsSlot"]


from .media import Media  # noqa: E402
from .cms_slot import CmsSlot  # noqa: E402
