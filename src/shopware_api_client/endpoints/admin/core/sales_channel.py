from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class SalesChannelBase(ApiModelBase[EndpointClass]):
    _identifier: str = "sales_channel"

    type_id: IdField
    language_id: IdField
    customer_group_id: IdField
    currency_id: IdField
    payment_method_id: IdField
    shipping_method_id: IdField
    country_id: IdField
    analytics_id: IdField | None = None
    navigation_category_id: IdField
    navigation_category_version_id: IdField | None = None
    navigation_category_depth: int | None = None
    footer_category_id: IdField | None = None
    footer_category_version_id: IdField | None = None
    service_category_id: IdField | None = None
    service_category_version_id: IdField | None = None
    mail_header_footer_id: IdField | None = None
    hreflang_default_domain_id: IdField | None = None
    name: str
    short_name: str | None = None
    tax_calculation_type: str | None = None
    access_key: str
    configuration: dict[str, Any] | None = None
    active: bool | None = None
    hreflang_active: bool | None = None
    maintenance: bool | None = None
    maintenance_ip_whitelist: list[str] | None = None
    custom_fields: dict[str, Any] | None = None
    payment_method_ids: list[IdField] | None = Field(default=None, exclude=True)
    home_cms_page_id: IdField | None = None
    home_cms_page_version_id: IdField | None = None
    home_slot_config: dict[str, Any] | None = None
    home_enabled: bool
    home_name: str | None = None
    home_meta_title: str | None = None
    home_meta_description: str | None = None
    home_keywords: str | None = None
    translated: dict[str, Any] | None = None


class SalesChannelRelations:
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


class SalesChannel(SalesChannelBase["SalesChannelEndpoint"], SalesChannelRelations):
    pass


class SalesChannelEndpoint(EndpointBase[SalesChannel]):
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
