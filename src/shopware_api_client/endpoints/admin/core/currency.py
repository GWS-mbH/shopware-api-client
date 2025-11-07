from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.currency import Currency as CurrencyBase


class Currency(CurrencyBase, AdminModel["CurrencyEndpoint"]):
    sales_channel_default_assignments: ManyRelation["SalesChannel"]
    orders: ManyRelation["Order"]
    sales_channels: ManyRelation["SalesChannel"]
    sales_channel_domains: ManyRelation["SalesChannelDomain"]
    promotion_discount_prices: ManyRelation["PromotionDiscountPrices"]
    product_exports: ManyRelation["ProductExport"]
    country_roundings: ManyRelation["CurrencyCountryRounding"]


class CurrencyEndpoint(AdminEndpoint[Currency]):
    name = "currency"
    path = "/currency"
    model_class = Currency


from .currency_country_rounding import CurrencyCountryRounding  # noqa: E402
from .order import Order  # noqa: E402
from .product_export import ProductExport  # noqa: E402
from .promotion_discount_prices import PromotionDiscountPrices  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .sales_channel_domain import SalesChannelDomain  # noqa: E402
