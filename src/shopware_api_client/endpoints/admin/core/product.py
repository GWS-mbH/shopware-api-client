from typing import Any

from pydantic import field_validator
from pydantic_core.core_schema import FieldValidationInfo

from shopware_api_client.base import AdminModel, AdminEndpoint
from ...base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.product import Product as ProductBase


class ProductValidators:
    @field_validator("name")
    def ensure_name_or_parent(cls, value: str | None, info: FieldValidationInfo, **kwargs: Any) -> str | None:
        if value is None and info.data["parent_id"] is None:
            raise ValueError("name may only be empty if parent_id is set")

        return value

    @field_validator("tax_id")
    def ensure_tax_id_or_parent(cls, value: IdField | None, info: FieldValidationInfo, **kwargs: Any) -> IdField | None:
        if value is None and info.data["parent_id"] is None:
            raise ValueError("tax_id may only be empty if parent_id is set")

        return value

    @field_validator("price")
    def ensure_price_or_parent(
        cls, value: list[dict[str, Any]] | None, info: FieldValidationInfo, **kwargs: Any
    ) -> list[dict[str, Any]] | None:
        if value is None and info.data["parent_id"] is None:
            raise ValueError("price may only be empty if parent_id is set")

        return value


class Product(ProductBase, AdminModel["ProductEndpoint"], ProductValidators):
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
    properties: ManyRelation["PropertyGroup"]
    categories: ManyRelation["Category"]
    streams: ManyRelation["ProductStream"]
    categories_ro: ManyRelation["Category"]
    tags: ManyRelation["Tag"]

    """
    Todo:
    custom_field_sets[CustomFieldSet]
    """


class ProductEndpoint(AdminEndpoint[Product]):
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
from .property_group import PropertyGroup  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .tag import Tag  # noqa: E402
from .tax import Tax  # noqa: E402
from .unit import Unit  # noqa: E402
