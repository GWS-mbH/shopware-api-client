from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.sales_channel_domain import SalesChannelDomainBase


class SalesChannelDomain(SalesChannelDomainBase, AdminModel["SalesChannelDomainEndpoint"]):
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    language: ForeignRelation["Language"] = Field(default=...)
    currency: ForeignRelation["Currency"] = Field(default=...)
    sales_channel_default_hreflang: ManyRelation["SalesChannel"] = Field(default=...)
    product_exports: ManyRelation["ProductExport"] = Field(default=...)

    """
    Not yet implemented Relations:
    snippet_set[SnippetSet]
    """


class SalesChannelDomainEndpoint(AdminEndpoint[SalesChannelDomain]):
    name = "sales_channel_domain"
    path = "/sales-channel-domain"
    model_class = SalesChannelDomain


from .currency import Currency  # noqa: E402
from .language import Language  # noqa: E402
from .product_export import ProductExport  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
