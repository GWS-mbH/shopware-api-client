from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.sales_channel import SalesChannel as SalesChannelBase


class SalesChannel(SalesChannelBase, AdminModel["SalesChannelEndpoint"]):
    type_id: IdField
    access_key: str
    currencies: ManyRelation["Currency"]
    languages: ManyRelation["Language"]
    countries: ManyRelation["Country"]
    payment_methods: ManyRelation["PaymentMethod"]
    shipping_methods: ManyRelation["ShippingMethod"]
    language: ForeignRelation["Language"]
    customer_group: ForeignRelation["CustomerGroup"]
    currency: ForeignRelation["Currency"]
    payment_method: ForeignRelation["PaymentMethod"]
    shipping_method: ForeignRelation["ShippingMethod"]
    country: ForeignRelation["Country"]
    orders: ManyRelation["Order"]
    customers: ManyRelation["Customer"]
    home_cms_page: ForeignRelation["CmsPage"]
    domains: ManyRelation["SalesChannelDomain"]
    navigation_category: ForeignRelation["Category"]
    footer_category: ForeignRelation["Category"]
    service_category: ForeignRelation["Category"]
    product_visibilities: ManyRelation["ProductVisibility"]
    hreflang_default_domain: ForeignRelation["SalesChannelDomain"]
    document_base_config_sales_channels: ManyRelation["DocumentBaseConfigSalesChannel"]
    product_reviews: ManyRelation["ProductReview"]
    seo_urls: ManyRelation["SeoUrl"]
    main_categories: ManyRelation["MainCategory"]
    product_exports: ManyRelation["ProductExport"]
    customer_groups_registrations: ManyRelation["CustomerGroup"]
    landing_pages: ManyRelation["LandingPage"]
    bound_customers: ManyRelation["Customer"]
    wishlists: ManyRelation["CustomerWishlist"]

    """
    Todo:
    type[SalesChannelType], system_configs[SystemConfig], mail_header_footer[MailHeaderFooter],
    newsletter_recipients[NewsletterRecipient], number_range_sales_channels[NumberRangeSalesChannel],
    promotion_sales_channels[PromotionSalesChannel], seo_url_templates[SeoUrlTemplate],
    analytics[SalesChannelAnalytics]
    """


class SalesChannelEndpoint(AdminEndpoint[SalesChannel]):
    name = "sales_channel"
    path = "/sales-channel"
    model_class = SalesChannel


from .category import Category  # noqa: E402
from .cms_page import CmsPage  # noqa: E402
from .country import Country  # noqa: E402
from .currency import Currency  # noqa: E402
from .customer import Customer  # noqa: E402
from .customer_group import CustomerGroup  # noqa: E402
from .customer_wishlist import CustomerWishlist  # noqa: E402
from .document_base_config_sales_channel import DocumentBaseConfigSalesChannel  # noqa: E402
from .landing_page import LandingPage  # noqa: E402
from .language import Language  # noqa: E402
from .main_category import MainCategory  # noqa: E402
from .order import Order  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .product_export import ProductExport  # noqa: E402
from .product_review import ProductReview  # noqa: E402
from .product_visibility import ProductVisibility  # noqa: E402
from .sales_channel_domain import SalesChannelDomain  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
