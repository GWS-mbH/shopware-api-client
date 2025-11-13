from shopware_api_client.models.category import CategoryBase


class Category(CategoryBase):
    parent: "Category | None" = None
    children: list["Category"]
    media: "Media | None" = None
    tags: list["Tag"] | None = None
    cms_page: "CmsPage | None" = None
    seo_urls: list["SeoUrl"] | None = None


from .cms_page import CmsPage  # noqa: E402
from .media import Media  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .tag import Tag  # noqa: E402
