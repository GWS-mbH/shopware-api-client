from shopware_api_client.models.sales_channel_domain import SalesChannelDomainBase


class SalesChannelDomain(SalesChannelDomainBase):
    language: "Language | None" = None
    currency: "Currency | None" = None
    sales_channel_default_hreflang: "SalesChannel | None" = None


from .currency import Currency  # noqa: E402
from .language import Language  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
