from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class SalesChannelDomainBase(ApiModelBase[EndpointClass]):
    _identifier: str = "sales_channel_domain"

    url: str
    sales_channel_id: IdField
    language_id: IdField
    currency_id: IdField
    snippet_set_id: IdField
    hreflang_use_only_locale: bool | None = None
    custom_fields: dict[str, Any] | None = None


class SalesChannelDomainRelations:
    sales_channel: ForeignRelation["SalesChannel"]
    language: ForeignRelation["Language"]
    currency: ForeignRelation["Currency"]
    sales_channel_default_hreflang: ManyRelation["SalesChannel"]
    product_exports: ManyRelation["ProductExport"]

    """
    Not yet implemented Relations:
    snippet_set[SnippetSet]
    """


class SalesChannelDomain(SalesChannelDomainBase["SalesChannelDomainEndpoint"], SalesChannelDomainRelations):
    pass


class SalesChannelDomainEndpoint(EndpointBase[SalesChannelDomain]):
    name = "sales_channel_domain"
    path = "/sales-channel-domain"
    model_class = SalesChannelDomain


from .currency import Currency  # noqa: E402
from .language import Language  # noqa: E402
from .product_export import ProductExport  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
