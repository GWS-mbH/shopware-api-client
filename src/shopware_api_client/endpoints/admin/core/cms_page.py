from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.cms_page import CmsPageBase


class CmsPage(CmsPageBase, AdminModel["CmsPageEndpoint"]):
    sections: ManyRelation["CmsSection"] = Field(default=...)
    preview_media: ForeignRelation["Media"] = Field(default=...)
    categories: ManyRelation["Category"] = Field(default=...)
    landing_pages: ManyRelation["LandingPage"] = Field(default=...)
    home_sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    products: ManyRelation["Product"] = Field(default=...)


class CmsPageEndpoint(AdminEndpoint[CmsPage]):
    name = "cms_page"
    path = "/cms-page"
    model_class = CmsPage


from .category import Category  # noqa: E402
from .cms_section import CmsSection  # noqa: E402
from .landing_page import LandingPage  # noqa: E402
from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
