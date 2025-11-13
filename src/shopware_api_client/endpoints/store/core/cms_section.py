from shopware_api_client.models.cms_section import CmsSectionBase


class CmsSection(CmsSectionBase):
    page: "CmsPage | None" = None
    background_media: "Media | None" = None
    blacks: list["CmsBlock"]


from .cms_block import CmsBlock  # noqa: E402
from .cms_page import CmsPage  # noqa: E402
from .media import Media  # noqa: E402
