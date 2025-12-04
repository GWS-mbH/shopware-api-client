from shopware_api_client.models.cms_page import CmsPageBase


class CmsPage(CmsPageBase):
    sections: list["CmsSection"]
    preview_media: "Media | None" = None
    landing_pages: list["LandingPage"] | None = None


from .cms_section import CmsSection  # noqa: E402
from .landing_page import LandingPage  # noqa: E402
from .media import Media  # noqa: E402
