from typing import Any
from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.price import Price
from shopware_api_client.structs.variant_listing_config import VariantListingConfig


class ProductBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product"

    parent_id: IdField | None = None
    parent_version_id: IdField | None = None
    manufacturer_id: IdField | None = None
    product_manufacturer_version_id: IdField | None = None
    unit_id: IdField | None = None
    tax_id: IdField | None = None
    cover_id: IdField | None = None
    product_media_version_id: IdField | None = None
    delivery_time_id: IdField | None = None
    feature_set_id: IdField | None = None
    canonical_product_id: IdField | None = None
    cms_page_id: IdField | None = None
    cms_page_version_id: IdField | None = None
    price: list[Price] | None = None
    product_number: str
    restock_time: int | None = None
    auto_increment: int | None = Field(default=None, exclude=True)
    active: bool | None = None
    available: bool | None = Field(default=None, exclude=True)
    is_closeout: bool | None = None
    variation: list[str] | None = None
    display_group: str | None = Field(default=None, exclude=True)
    variant_listing_config: VariantListingConfig | None = None
    variant_restrictions: dict[str, Any] | None = Field(default=None)
    manufacturer_number: str | None = None
    ean: str | None = None
    purchase_steps: int | None = None
    max_purchase: int | None = None
    min_purchase: int | None = None
    purchase_unit: float | None = None
    reference_unit: float | None = None
    shipping_free: bool | None = None
    purchase_prices: list[Price] | None = None
    mark_as_topseller: bool | None = None
    weight: float | None = None
    width: float | None = None
    height: float | None = None
    length: float | None = None
    release_date: AwareDatetime | None = None
    rating_average: float | None = Field(default=None, exclude=True)
    category_tree: list[IdField] | None = Field(default=None, exclude=True)
    property_ids: list[IdField] | None = Field(default=None, exclude=True)
    option_ids: list[IdField] | None = Field(default=None, exclude=True)
    stream_ids: list[IdField] | None = Field(default=None, exclude=True)
    tag_ids: list[IdField] | None = Field(default=None, exclude=True)
    category_ids: list[IdField] | None = Field(default=None, exclude=True)
    child_count: int | None = Field(default=None, exclude=True)
    custom_field_set_selection_active: bool | None = None
    sales: int | None = Field(default=None, exclude=True)
    states: list[str] | None = Field(default=None, exclude=True)
    meta_description: str | None = None
    name: str | None = None
    keywords: str | None = None
    description: str | None = None
    meta_title: str | None = None
    pack_unit: str | None = None
    pack_unit_plural: str | None = None
    slot_config: dict[str, Any] | list | None = Field(default=None)
    custom_search_keywords: list[str] | None = None
    available_stock: int | None = Field(default=None, exclude=True)
    stock: int | None = None
