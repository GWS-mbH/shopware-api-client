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
        CustomerWishlistProduct,
        DeliveryTime,
        MainCategory,
        OrderLineItem,
        ProductConfiguratorSetting,
        ProductCrossSelling,
        ProductCrossSellingAssignedProducts,
        ProductDownload,
        ProductFeatureSet,
        ProductManufacturer,
        ProductMedia,
        ProductPrice,
        ProductReview,
        ProductSearchKeyword,
        ProductStream,
        ProductVisibility,
        PropertyGroupOption,
        SeoUrl,
        Tag,
        Tax,
        Unit,
    )


class ProductBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    parent_id: IdField | None = Field(
        default=None, serialization_alias="parentId", validation_alias=AliasChoices("parent_id", "parentId")
    )
    parent_version_id: IdField | None = Field(
        default=None,
        serialization_alias="parentVersionId",
        validation_alias=AliasChoices("parent_version_id", "parentVersionId"),
    )
    manufacturer_id: IdField | None = Field(
        default=None,
        serialization_alias="manufacturerId",
        validation_alias=AliasChoices("manufacturer_id", "manufacturerId"),
    )
    product_manufacturer_version_id: IdField | None = Field(
        default=None, serialization_alias="productManufacturerVersionId"
    )
    unit_id: IdField | None = Field(
        default=None, serialization_alias="unitId", validation_alias=AliasChoices("unit_id", "unitId")
    )
    tax_id: IdField = Field(..., serialization_alias="taxId", validation_alias=AliasChoices("tax_id", "taxId"))
    cover_id: IdField | None = Field(
        default=None, serialization_alias="coverId", validation_alias=AliasChoices("cover_id", "coverId")
    )
    product_media_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productMediaVersionId",
        validation_alias=AliasChoices("product_media_version_id", "productMediaVersionId"),
    )
    delivery_time_id: IdField | None = Field(
        default=None,
        serialization_alias="deliveryTimeId",
        validation_alias=AliasChoices("delivery_time_id", "deliveryTimeId"),
    )
    feature_set_id: IdField | None = Field(
        default=None,
        serialization_alias="featureSetId",
        validation_alias=AliasChoices("feature_set_id", "featureSetId"),
    )
    canonical_product_id: IdField | None = Field(
        default=None,
        serialization_alias="canonicalProductId",
        validation_alias=AliasChoices("canonical_product_id", "canonicalProductId"),
    )
    cms_page_id: IdField | None = Field(
        default=None, serialization_alias="cmsPageId", validation_alias=AliasChoices("cms_page_id", "cmsPageId")
    )
    cms_page_version_id: IdField | None = Field(
        default=None,
        serialization_alias="cmsPageVersionId",
        validation_alias=AliasChoices("cms_page_version_id", "cmsPageVersionId"),
    )
    price: list[dict[str, Any]]
    product_number: str = Field(
        ..., serialization_alias="productNumber", validation_alias=AliasChoices("product_number", "productNumber")
    )
    restock_time: int | None = Field(
        default=None, serialization_alias="restockTime", validation_alias=AliasChoices("restock_time", "restockTime")
    )
    auto_increment: int | None = Field(
        default=None,
        serialization_alias="autoIncrement",
        validation_alias=AliasChoices("auto_increment", "autoIncrement"),
        exclude=True,
    )
    active: bool | None = None
    available: bool | None = Field(default=None, exclude=True)
    is_closeout: bool | None = Field(
        default=None, serialization_alias="isCloseout", validation_alias=AliasChoices("is_closeout", "isCloseout")
    )
    variation: list[str] | None = None
    display_group: str | None = Field(
        default=None,
        serialization_alias="displayGroup",
        validation_alias=AliasChoices("display_group", "displayGroup"),
        exclude=True,
    )
    variant_listing_config: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="variantListingConfig",
        validation_alias=AliasChoices("variant_listing_config", "variantListingConfig"),
    )
    variant_restrictions: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="variantRestrictions",
        validation_alias=AliasChoices("variant_restrictions", "variantRestrictions"),
    )
    manufacturer_number: str | None = Field(
        default=None,
        serialization_alias="manufacturerNumber",
        validation_alias=AliasChoices("manufacturer_number", "manufacturerNumber"),
    )
    ean: str | None = None
    purchase_steps: int | None = Field(
        default=None,
        serialization_alias="purchaseSteps",
        validation_alias=AliasChoices("purchase_steps", "purchaseSteps"),
    )
    max_purchase: int | None = Field(
        default=None, serialization_alias="maxPurchase", validation_alias=AliasChoices("max_purchase", "maxPurchase")
    )
    min_purchase: int | None = Field(
        default=None, serialization_alias="minPurchase", validation_alias=AliasChoices("min_purchase", "minPurchase")
    )
    purchase_unit: float | None = Field(
        default=None, serialization_alias="purchaseUnit", validation_alias=AliasChoices("purchase_unit", "purchaseUnit")
    )
    reference_unit: float | None = Field(
        default=None,
        serialization_alias="referenceUnit",
        validation_alias=AliasChoices("reference_unit", "referenceUnit"),
    )
    shipping_free: bool | None = Field(
        default=None, serialization_alias="shippingFree", validation_alias=AliasChoices("shipping_free", "shippingFree")
    )
    purchase_prices: list[dict[str, Any]] | None = Field(
        default=None,
        serialization_alias="purchasePrices",
        validation_alias=AliasChoices("purchase_prices", "purchasePrices"),
    )
    mark_as_topseller: bool | None = Field(
        default=None,
        serialization_alias="markAsTopseller",
        validation_alias=AliasChoices("mark_as_topseller", "markAsTopseller"),
    )
    weight: float | None = None
    width: float | None = None
    height: float | None = None
    length: float | None = None
    release_date: AwareDatetime | None = Field(
        default=None, serialization_alias="releaseDate", validation_alias=AliasChoices("release_date", "releaseDate")
    )
    rating_average: float | None = Field(
        default=None,
        serialization_alias="ratingAverage",
        validation_alias=AliasChoices("rating_average", "ratingAverage"),
        exclude=True,
    )
    category_tree: list[IdField] | None = Field(
        default=None,
        serialization_alias="categoryTree",
        validation_alias=AliasChoices("category_tree", "categoryTree"),
        exclude=True,
    )
    property_ids: list[IdField] | None = Field(
        default=None,
        serialization_alias="propertyIds",
        validation_alias=AliasChoices("property_ids", "propertyIds"),
        exclude=True,
    )
    option_ids: list[IdField] | None = Field(
        default=None,
        serialization_alias="optionIds",
        validation_alias=AliasChoices("option_ids", "optionIds"),
        exclude=True,
    )
    stream_ids: list[IdField] | None = Field(
        default=None,
        serialization_alias="streamIds",
        validation_alias=AliasChoices("stream_ids", "streamIds"),
        exclude=True,
    )
    tag_ids: list[IdField] | None = Field(
        default=None, serialization_alias="tagIds", validation_alias=AliasChoices("tag_ids", "tagIds"), exclude=True
    )
    category_ids: list[IdField] | None = Field(
        default=None,
        serialization_alias="categoryIds",
        validation_alias=AliasChoices("category_ids", "categoryIds"),
        exclude=True,
    )
    child_count: int | None = Field(
        default=None,
        serialization_alias="childCount",
        validation_alias=AliasChoices("child_count", "childCount"),
        exclude=True,
    )
    custom_field_set_selection_active: bool | None = Field(
        default=None, serialization_alias="customFieldSetSelectionActive"
    )
    sales: int | None = Field(default=None, exclude=True)
    states: list[str] | None = Field(default=None, exclude=True)
    meta_description: str | None = Field(
        default=None,
        serialization_alias="metaDescription",
        validation_alias=AliasChoices("meta_description", "metaDescription"),
    )
    name: str
    keywords: str | None = None
    description: str | None = None
    meta_title: str | None = Field(
        default=None, serialization_alias="metaTitle", validation_alias=AliasChoices("meta_title", "metaTitle")
    )
    pack_unit: str | None = Field(
        default=None, serialization_alias="packUnit", validation_alias=AliasChoices("pack_unit", "packUnit")
    )
    pack_unit_plural: str | None = Field(
        default=None,
        serialization_alias="packUnitPlural",
        validation_alias=AliasChoices("pack_unit_plural", "packUnitPlural"),
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    slot_config: dict[str, Any] | None = Field(
        default=None, serialization_alias="slotConfig", validation_alias=AliasChoices("slot_config", "slotConfig")
    )
    custom_search_keywords: list[dict[str, Any]] | None = Field(
        default=None, serialization_alias="customSearchKeywords"
    )
    available_stock: int | None = Field(
        default=None,
        serialization_alias="availableStock",
        validation_alias=AliasChoices("available_stock", "availableStock"),
    )
    stock: int
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


class ProductRelations:
    downloads: ClassVar[ManyRelation["ProductDownload"]] = ManyRelation("ProductDownload", "downloads")
    parent: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "parent_id")
    children: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "children")
    delivery_time: ClassVar[ForeignRelation["DeliveryTime"]] = ForeignRelation("DeliveryTime", "delivery_time_id")
    tax: ClassVar[ForeignRelation["Tax"]] = ForeignRelation("Tax", "tax_id")
    manufacturer: ClassVar[ForeignRelation["ProductManufacturer"]] = ForeignRelation(
        "ProductManufacturer", "manufacturer_id"
    )
    unit: ClassVar[ForeignRelation["Unit"]] = ForeignRelation("Unit", "unit_id")
    cover: ClassVar[ForeignRelation["ProductMedia"]] = ForeignRelation("ProductMedia", "cover_id")
    feature_set: ClassVar[ForeignRelation["ProductFeatureSet"]] = ForeignRelation("ProductFeatureSet", "feature_set_id")
    cms_page: ClassVar[ForeignRelation["CmsPage"]] = ForeignRelation("CmsPage", "cms_page_id")
    canonical_product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "canonical_product_id")
    prices: ClassVar[ManyRelation["ProductPrice"]] = ManyRelation("ProductPrices", "prices")
    media: ClassVar[ManyRelation["ProductMedia"]] = ManyRelation("ProductMedia", "media")
    cross_sellings: ClassVar[ManyRelation["ProductCrossSelling"]] = ManyRelation("ProductCrossSelling", "crossSellings")
    cross_selling_assigned_products: ClassVar[ManyRelation["ProductCrossSellingAssignedProducts"]] = ManyRelation(
        "ProductCrossSellingAssignedProducts", "crossSellingAssignedProducts"
    )
    configurator_settings: ClassVar[ManyRelation["ProductConfiguratorSetting"]] = ManyRelation(
        "ProductConfiguratorSetting", "configuratorSettings"
    )
    visibilities: ClassVar[ManyRelation["ProductVisibility"]] = ManyRelation("ProductVisibility", "visibilities")
    search_keywords: ClassVar[ManyRelation["ProductSearchKeyword"]] = ManyRelation(
        "ProductSearchKeyword", "searchKeywords"
    )
    product_reviews: ClassVar[ManyRelation["ProductReview"]] = ManyRelation("ProductReview", "productReviews")
    main_categories: ClassVar[ManyRelation["MainCategory"]] = ManyRelation("MainCategory", "mainCategories")
    seo_urls: ClassVar[ManyRelation["SeoUrl"]] = ManyRelation("SeoUrl", "seoUrls")
    order_line_items: ClassVar[ManyRelation["OrderLineItem"]] = ManyRelation("OrderLineItem", "orderLineItems")
    wishlists: ClassVar[ManyRelation["CustomerWishlistProduct"]] = ManyRelation("CustomerWishlistProduct", "wishlists")
    options: ClassVar[ManyRelation["PropertyGroupOption"]] = ManyRelation("PropertyGroupOption", "options")
    properties: ClassVar[ManyRelation["PropertyGroupOption"]] = ManyRelation("PropertyGroupOption", "properties")
    categories: ClassVar[ManyRelation["Category"]] = ManyRelation("Category", "categories")
    streams: ClassVar[ManyRelation["ProductStream"]] = ManyRelation("ProductStream", "streams")
    categories_ro: ClassVar[ManyRelation["Category"]] = ManyRelation("Category", "categories-ro")
    tags: ClassVar[ManyRelation["Tag"]] = ManyRelation("Tag", "tags")

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


registry.register_admin(ProductEndpoint)
