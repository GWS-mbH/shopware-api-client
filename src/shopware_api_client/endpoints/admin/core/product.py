from typing import Any

from pydantic import AwareDatetime, Field, field_validator
from pydantic_core.core_schema import FieldValidationInfo

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class ProductBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product"

    version_id: IdField | None = None
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
    price: list[dict[str, Any]] | None = None
    product_number: str
    restock_time: int | None = None
    auto_increment: int | None = Field(default=None, exclude=True)
    active: bool | None = None
    available: bool | None = Field(default=None, exclude=True)
    is_closeout: bool | None = None
    variation: list[str] | None = None
    display_group: str | None = Field(default=None, exclude=True)
    variant_listing_config: dict[str, Any] | None = None
    variant_restrictions: dict[str, Any] | None = None
    manufacturer_number: str | None = None
    ean: str | None = None
    purchase_steps: int | None = None
    max_purchase: int | None = None
    min_purchase: int | None = None
    purchase_unit: float | None = None
    reference_unit: float | None = None
    shipping_free: bool | None = None
    purchase_prices: list[dict[str, Any]] | None = None
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
    custom_fields: dict[str, Any] | None = None
    slot_config: dict[str, Any] | list | None = None
    custom_search_keywords: list[str] | None = None
    available_stock: int | None = Field(default=None, exclude=True)
    stock: int | None = None
    translated: dict[str, Any] | None = None

    @field_validator('name')
    def ensure_name_or_parent(cls, value: str | None, info: FieldValidationInfo, **kwargs: Any) -> str | None:
        if value is None and info.data['parent_id'] is None:
            raise ValueError('name may only be empty if parent_id is set')

        return value

    @field_validator('tax_id')
    def ensure_tax_id_or_parent(cls, value: IdField | None, info: FieldValidationInfo, **kwargs: Any) -> IdField | None:
        if value is None and info.data['parent_id'] is None:
            raise ValueError('tax_id may only be empty if parent_id is set')

        return value

    @field_validator('price')
    def ensure_price_or_parent(cls, value: list[dict[str, Any]] | None, info: FieldValidationInfo, **kwargs: Any) -> list[dict[str, Any]] | None:
        if value is None and info.data['parent_id'] is None:
            raise ValueError('price may only be empty if parent_id is set')

        return value

class ProductRelations:
    downloads: ManyRelation["ProductDownload"]
    parent: ForeignRelation["Product"]
    children: ManyRelation["Product"]
    delivery_time: ForeignRelation["DeliveryTime"]
    tax: ForeignRelation["Tax"]
    manufacturer: ForeignRelation["ProductManufacturer"]
    unit: ForeignRelation["Unit"]
    cover: ForeignRelation["ProductMedia"]
    feature_set: ForeignRelation["ProductFeatureSet"]
    cms_page: ForeignRelation["CmsPage"]
    canonical_product: ForeignRelation["Product"]
    prices: ManyRelation["ProductPrice"]
    media: ManyRelation["ProductMedia"]
    cross_sellings: ManyRelation["ProductCrossSelling"]
    cross_selling_assigned_products: ManyRelation["ProductCrossSellingAssignedProducts"]
    configurator_settings: ManyRelation["ProductConfiguratorSetting"]
    visibilities: ManyRelation["ProductVisibility"]
    search_keywords: ManyRelation["ProductSearchKeyword"]
    product_reviews: ManyRelation["ProductReview"]
    main_categories: ManyRelation["MainCategory"]
    seo_urls: ManyRelation["SeoUrl"]
    order_line_items: ManyRelation["OrderLineItem"]
    wishlists: ManyRelation["CustomerWishlistProduct"]
    options: ManyRelation["PropertyGroupOption"]
    properties: ManyRelation["PropertyGroupOption"]
    categories: ManyRelation["Category"]
    streams: ManyRelation["ProductStream"]
    categories_ro: ManyRelation["Category"]
    tags: ManyRelation["Tag"]

    """
    Todo:
    custom_field_sets[CustomFieldSet]
    """


class Product(ProductBase["ProductEndpoint"], ProductRelations):
    pass


class ProductEndpoint(EndpointBase[Product]):
    name = "product"
    path = "/product"
    model_class = Product


from .category import Category  # noqa: E402
from .cms_page import CmsPage  # noqa: E402
from .customer_wishlist_product import CustomerWishlistProduct  # noqa: E402
from .delivery_time import DeliveryTime  # noqa: E402
from .main_category import MainCategory  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
from .product_configurator_setting import ProductConfiguratorSetting  # noqa: E402
from .product_cross_selling import ProductCrossSelling  # noqa: E402
from .product_cross_selling_assigned_products import ProductCrossSellingAssignedProducts  # noqa: E402
from .product_download import ProductDownload  # noqa: E402
from .product_feature_set import ProductFeatureSet  # noqa: E402
from .product_manufacturer import ProductManufacturer  # noqa: E402
from .product_media import ProductMedia  # noqa: E402
from .product_price import ProductPrice  # noqa: E402
from .product_review import ProductReview  # noqa: E402
from .product_search_keyword import ProductSearchKeyword  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
from .product_visibility import ProductVisibility  # noqa: E402
from .property_group_option import PropertyGroupOption  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .tag import Tag  # noqa: E402
from .tax import Tax  # noqa: E402
from .unit import Unit  # noqa: E402
