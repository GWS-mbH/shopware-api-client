from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import (
        Category,
        CmsPage,
        Country,
        Currency,
        Customer,
        CustomerGroup,
        CustomerWishlist,
        DocumentBaseConfigSalesChannel,
        LandingPage,
        Language,
        MainCategory,
        Order,
        PaymentMethod,
        ProductExport,
        ProductReview,
        ProductVisibility,
        SalesChannelDomain,
        SeoUrl,
        ShippingMethod,
    )


class SalesChannelBase(ApiModelBase[EndpointClass]):
    _identifier: str = "sales_channel"

    type_id: IdField = Field(..., serialization_alias="typeId", validation_alias=AliasChoices("type_id", "typeId"))
    language_id: IdField = Field(
        ..., serialization_alias="languageId", validation_alias=AliasChoices("language_id", "languageId")
    )
    customer_group_id: IdField = Field(
        ...,
        serialization_alias="customerGroupId",
        validation_alias=AliasChoices("customer_group_id", "customerGroupId"),
    )
    currency_id: IdField = Field(
        ..., serialization_alias="currencyId", validation_alias=AliasChoices("currency_id", "currencyId")
    )
    payment_method_id: IdField = Field(
        ...,
        serialization_alias="paymentMethodId",
        validation_alias=AliasChoices("payment_method_id", "paymentMethodId"),
    )
    shipping_method_id: IdField = Field(
        ...,
        serialization_alias="shippingMethodId",
        validation_alias=AliasChoices("shipping_method_id", "shippingMethodId"),
    )
    country_id: IdField = Field(
        ..., serialization_alias="countryId", validation_alias=AliasChoices("country_id", "countryId")
    )
    analytics_id: IdField | None = Field(
        default=None, serialization_alias="analyticsId", validation_alias=AliasChoices("analytics_id", "analyticsId")
    )
    navigation_category_id: IdField = Field(
        ...,
        serialization_alias="navigationCategoryId",
        validation_alias=AliasChoices("navigation_category_id", "navigationCategoryId"),
    )
    navigation_category_version_id: IdField | None = Field(
        default=None, serialization_alias="navigationCategoryVersionId"
    )
    navigation_category_depth: int | None = Field(
        default=None,
        serialization_alias="navigationCategoryDepth",
        validation_alias=AliasChoices("navigation_category_depth", "navigationCategoryDepth"),
    )
    footer_category_id: IdField | None = Field(
        default=None,
        serialization_alias="footerCategoryId",
        validation_alias=AliasChoices("footer_category_id", "footerCategoryId"),
    )
    footer_category_version_id: IdField | None = Field(
        default=None,
        serialization_alias="footerCategoryVersionId",
        validation_alias=AliasChoices("footer_category_version_id", "footerCategoryVersionId"),
    )
    service_category_id: IdField | None = Field(
        default=None,
        serialization_alias="serviceCategoryId",
        validation_alias=AliasChoices("service_category_id", "serviceCategoryId"),
    )
    service_category_version_id: IdField | None = Field(
        default=None,
        serialization_alias="serviceCategoryVersionId",
        validation_alias=AliasChoices("service_category_version_id", "serviceCategoryVersionId"),
    )
    mail_header_footer_id: IdField | None = Field(
        default=None,
        serialization_alias="mailHeaderFooterId",
        validation_alias=AliasChoices("mail_header_footer_id", "mailHeaderFooterId"),
    )
    hreflang_default_domain_id: IdField | None = Field(
        default=None,
        serialization_alias="hreflangDefaultDomainId",
        validation_alias=AliasChoices("hreflang_default_domain_id", "hreflangDefaultDomainId"),
    )
    name: str
    short_name: str | None = Field(
        default=None, serialization_alias="shortName", validation_alias=AliasChoices("short_name", "shortName")
    )
    tax_calculation_type: str | None = Field(
        default=None,
        serialization_alias="taxCalculationType",
        validation_alias=AliasChoices("tax_calculation_type", "taxCalculationType"),
    )
    access_key: str = Field(
        ..., serialization_alias="accessKey", validation_alias=AliasChoices("access_key", "accessKey")
    )
    configuration: dict[str, Any] | None = None
    active: bool | None = None
    hreflang_active: bool | None = Field(
        default=None,
        serialization_alias="hreflangActive",
        validation_alias=AliasChoices("hreflang_active", "hreflangActive"),
    )
    maintenance: bool | None = None
    maintenance_ip_whitelist: list[dict[str, Any]] | None = Field(
        default=None, serialization_alias="maintenanceIpWhitelist"
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    payment_method_ids: list[IdField] | None = Field(
        default=None,
        serialization_alias="paymentMethodIds",
        validation_alias=AliasChoices("payment_method_ids", "paymentMethodIds"),
        exclude=True,
    )
    home_cms_page_id: IdField | None = Field(
        default=None,
        serialization_alias="homeCmsPageId",
        validation_alias=AliasChoices("home_cms_page_id", "homeCmsPageId"),
    )
    home_cms_page_version_id: IdField | None = Field(
        default=None,
        serialization_alias="homeCmsPageVersionId",
        validation_alias=AliasChoices("home_cms_page_version_id", "homeCmsPageVersionId"),
    )
    home_slot_config: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="homeSlotConfig",
        validation_alias=AliasChoices("home_slot_config", "homeSlotConfig"),
    )
    home_enabled: bool = Field(
        ..., serialization_alias="homeEnabled", validation_alias=AliasChoices("home_enabled", "homeEnabled")
    )
    home_name: str | None = Field(
        default=None, serialization_alias="homeName", validation_alias=AliasChoices("home_name", "homeName")
    )
    home_meta_title: str | None = Field(
        default=None,
        serialization_alias="homeMetaTitle",
        validation_alias=AliasChoices("home_meta_title", "homeMetaTitle"),
    )
    home_meta_description: str | None = Field(
        default=None,
        serialization_alias="homeMetaDescription",
        validation_alias=AliasChoices("home_meta_description", "homeMetaDescription"),
    )
    home_keywords: str | None = Field(
        default=None, serialization_alias="homeKeywords", validation_alias=AliasChoices("home_keywords", "homeKeywords")
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )
    translated: dict[str, Any] | None = None


class SalesChannelRelations:
    currencies: ClassVar[ManyRelation["Currency"]] = ManyRelation("Currency", "currencies")
    languages: ClassVar[ManyRelation["Language"]] = ManyRelation("Language", "languages")
    countries: ClassVar[ManyRelation["Country"]] = ManyRelation("Country", "countries")
    payment_methods: ClassVar[ManyRelation["PaymentMethod"]] = ManyRelation("PaymentMethod", "paymentMethods")
    shipping_methods: ClassVar[ManyRelation["ShippingMethod"]] = ManyRelation("ShippingMethod", "shippingMethods")
    language: ClassVar[ForeignRelation["Language"]] = ForeignRelation("Language", "language_id")
    customer_group: ClassVar[ForeignRelation["CustomerGroup"]] = ForeignRelation("CustomerGroup", "customer_group_id")
    currency: ClassVar[ForeignRelation["Currency"]] = ForeignRelation("Currency", "currency_id")
    payment_method: ClassVar[ForeignRelation["PaymentMethod"]] = ForeignRelation("PaymentMethod", "payment_method_id")
    shipping_method: ClassVar[ForeignRelation["ShippingMethod"]] = ForeignRelation(
        "ShippingMethod", "shipping_method_id"
    )
    country: ClassVar[ForeignRelation["Country"]] = ForeignRelation("Country", "country_id")
    orders: ClassVar[ManyRelation["Order"]] = ManyRelation("Order", "orders")
    customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "customers")
    home_cms_page: ClassVar[ForeignRelation["CmsPage"]] = ForeignRelation("CmsPage", "home_cms_page_id")
    domains: ClassVar[ManyRelation["SalesChannelDomain"]] = ManyRelation("SalesChannelDomain", "domains")
    navigation_category: ClassVar[ForeignRelation["Category"]] = ForeignRelation("Category", "navigation_category_id")
    footer_category: ClassVar[ForeignRelation["Category"]] = ForeignRelation("Category", "footer_category_id")
    service_category: ClassVar[ForeignRelation["Category"]] = ForeignRelation("Category", "service_category_id")
    product_visibilities: ClassVar[ManyRelation["ProductVisibility"]] = ManyRelation(
        "ProductVisibility", "productVisibilities"
    )
    hreflang_default_domain: ClassVar[ForeignRelation["SalesChannelDomain"]] = ForeignRelation(
        "SalesChannelDomain", "hreflang_default_domain_id"
    )
    document_base_config_sales_channels: ClassVar[ManyRelation["DocumentBaseConfigSalesChannel"]] = ManyRelation(
        "DocumentBaseConfigSalesChannel", "documentBaseConfigSalesChannels"
    )
    product_reviews: ClassVar[ManyRelation["ProductReview"]] = ManyRelation("ProductReview", "productReviews")
    seo_urls: ClassVar[ManyRelation["SeoUrl"]] = ManyRelation("SeoUrl", "seoUrls")
    main_categories: ClassVar[ManyRelation["MainCategory"]] = ManyRelation("MainCategory", "mainCategories")
    product_exports: ClassVar[ManyRelation["ProductExport"]] = ManyRelation("ProductExport", "productExports")
    customer_groups_registrations: ClassVar[ManyRelation["CustomerGroup"]] = ManyRelation(
        "CustomerGroup", "customerGroupsRegistrations"
    )
    landing_pages: ClassVar[ManyRelation["LandingPage"]] = ManyRelation("LandingPage", "landingPages")
    bound_customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "boundCustomers")
    wishlists: ClassVar[ManyRelation["CustomerWishlist"]] = ManyRelation("CustomerWishlist", "wishlists")

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


registry.register_admin(SalesChannelEndpoint)
