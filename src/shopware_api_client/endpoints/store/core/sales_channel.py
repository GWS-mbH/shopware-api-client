from shopware_api_client.models.sales_channel import SalesChannelBase


class SalesChannel(SalesChannelBase):
    language: "Language | None" = None
    currency: "Currency | None" = None
    payment_method: "PaymentMethod | None" = None
    shipping_method: "ShippingMethod | None" = None
    country: "Country | None" = None
    domains: list["SalesChannelDomain"] | None = None
    navigation_category: "Category | None" = None
    footer_category: "Category | None" = None
    service_category: "Category | None" = None
    hreflang_default_domain: "SalesChannelDomain | None" = None


from .category import Category  # noqa: E402
from .country import Country  # noqa: E402
from .currency import Currency  # noqa: E402
from .language import Language  # noqa: E402
from .sales_channel_domain import SalesChannelDomain  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
