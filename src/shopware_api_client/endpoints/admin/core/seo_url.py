from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.seo_url import SeoUrl as SeoUrlBase


class SeoUrl(SeoUrlBase, AdminModel["SeoUrlEndpoint"]):
    language: ForeignRelation["Language"]
    sales_channel: ForeignRelation["SalesChannel"]


class SeoUrlEndpoint(AdminEndpoint[SeoUrl]):
    name = "seo_url"
    path = "/seo-url"
    model_class = SeoUrl


from .language import Language  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
