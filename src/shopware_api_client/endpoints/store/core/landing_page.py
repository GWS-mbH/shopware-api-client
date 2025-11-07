from shopware_api_client.models.landing_page import LandingPage as LandingPageBase


class LandingPage(LandingPageBase):
    cms_page: "CmsPage | None" = None
    seo_urls: list["SeoUrl"] | None = None


from .cms_page import CmsPage  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
