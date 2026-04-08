from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.sales_channel import SalesChannelBase


class SalesChannel(SalesChannelBase, AdminModel["SalesChannelEndpoint"]):
    type_id: IdField
    access_key: str
    currencies: ManyRelation["Currency"] = Field(default=...)
    languages: ManyRelation["Language"] = Field(default=...)
    countries: ManyRelation["Country"] = Field(default=...)
    payment_methods: ManyRelation["PaymentMethod"] = Field(default=...)
    shipping_methods: ManyRelation["ShippingMethod"] = Field(default=...)
    language: ForeignRelation["Language"] = Field(default=...)
    customer_group: ForeignRelation["CustomerGroup"] = Field(default=...)
    currency: ForeignRelation["Currency"] = Field(default=...)
    payment_method: ForeignRelation["PaymentMethod"] = Field(default=...)
    shipping_method: ForeignRelation["ShippingMethod"] = Field(default=...)
    country: ForeignRelation["Country"] = Field(default=...)
    orders: ManyRelation["Order"] = Field(default=...)
    customers: ManyRelation["Customer"] = Field(default=...)
    home_cms_page: ForeignRelation["CmsPage"] = Field(default=...)
    domains: ManyRelation["SalesChannelDomain"] = Field(default=...)
    navigation_category: ForeignRelation["Category"] = Field(default=...)
    footer_category: ForeignRelation["Category"] = Field(default=...)
    service_category: ForeignRelation["Category"] = Field(default=...)
    product_visibilities: ManyRelation["ProductVisibility"] = Field(default=...)
    hreflang_default_domain: ForeignRelation["SalesChannelDomain"] = Field(default=...)
    document_base_config_sales_channels: ManyRelation["DocumentBaseConfigSalesChannel"] = Field(default=...)
    product_reviews: ManyRelation["ProductReview"] = Field(default=...)
    seo_urls: ManyRelation["SeoUrl"] = Field(default=...)
    main_categories: ManyRelation["MainCategory"] = Field(default=...)
    product_exports: ManyRelation["ProductExport"] = Field(default=...)
    customer_groups_registrations: ManyRelation["CustomerGroup"] = Field(default=...)
    landing_pages: ManyRelation["LandingPage"] = Field(default=...)
    bound_customers: ManyRelation["Customer"] = Field(default=...)
    wishlists: ManyRelation["CustomerWishlist"] = Field(default=...)

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
