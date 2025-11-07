from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.landing_page import LandingPage as LandingPageBase


class LandingPage(LandingPageBase, AdminModel["LandingPageEndpoint"]):
    tags: ManyRelation["Tag"]
    cms_page: ForeignRelation["CmsPage"]
    sales_channels: ManyRelation["SalesChannel"]
    seo_urls: ManyRelation["SeoUrl"]


class LandingPageEndpoint(AdminEndpoint[LandingPage]):
    name = "landing_page"
    path = "/landing-page"
    model_class = LandingPage


from .cms_page import CmsPage  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .tag import Tag  # noqa: E402
