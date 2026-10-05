from typing import Annotated, Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class SalesChannelBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "sales_channel"

    language_id: Annotated[IdField, RefersTo("language")]
    customer_group_id: Annotated[IdField, RefersTo("customer_group")]
    currency_id: Annotated[IdField, RefersTo("currency")]
    payment_method_id: Annotated[IdField, RefersTo("payment_method")]
    shipping_method_id: Annotated[IdField, RefersTo("shipping_method")]
    country_id: Annotated[IdField, RefersTo("country")]
    analytics_id: IdField | None = None
    navigation_category_id: Annotated[IdField, RefersTo("category")]
    navigation_category_version_id: IdField | None = None
    navigation_category_depth: int | None = None
    footer_category_id: Annotated[IdField | None, RefersTo("category")] = None
    footer_category_version_id: IdField | None = None
    service_category_id: Annotated[IdField | None, RefersTo("category")] = None
    service_category_version_id: IdField | None = None
    mail_header_footer_id: IdField | None = None
    hreflang_default_domain_id: Annotated[IdField | None, RefersTo("sales_channel_domain")] = None
    name: str
    short_name: str | None = None
    tax_calculation_type: str | None = None
    configuration: dict[str, Any] | None = Field(default=None)
    active: bool | None = None
    hreflang_active: bool | None = None
    maintenance: bool | None = None
    maintenance_ip_whitelist: list[str] | None = None
    payment_method_ids: list[IdField] | None = Field(default=None, exclude=True)
    home_cms_page_id: Annotated[IdField | None, RefersTo("cms_page")] = None
    home_cms_page_version_id: IdField | None = None
    home_slot_config: dict[str, Any] | None = Field(default=None)
    home_enabled: bool
    home_name: str | None = None
    home_meta_title: str | None = None
    home_meta_description: str | None = None
    home_keywords: str | None = None
