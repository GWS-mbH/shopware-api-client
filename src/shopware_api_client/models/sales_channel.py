from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class SalesChannelBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "sales_channel"

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
    configuration: dict[str, Any] | None = Field(default=None)
    active: bool | None = None
    hreflang_active: bool | None = None
    maintenance: bool | None = None
    maintenance_ip_whitelist: list[str] | None = None
    payment_method_ids: list[IdField] | None = Field(default=None, exclude=True)
    home_cms_page_id: IdField | None = None
    home_cms_page_version_id: IdField | None = None
    home_slot_config: dict[str, Any] | None = Field(default=None)
    home_enabled: bool
    home_name: str | None = None
    home_meta_title: str | None = None
    home_meta_description: str | None = None
    home_keywords: str | None = None
