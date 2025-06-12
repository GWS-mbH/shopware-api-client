from ....base import EndpointBase
from ....endpoints.admin.core.category import CategoryBase
from ....endpoints.admin.core.cms_page import CmsPageBase
from ....endpoints.admin.core.delivery_time import DeliveryTimeBase
from ....endpoints.admin.core.main_category import MainCategoryBase
from ....endpoints.admin.core.product import ProductBase
from ....endpoints.admin.core.product_configurator_setting import ProductConfiguratorSettingBase
from ....endpoints.admin.core.product_cross_selling import ProductCrossSellingBase
from ....endpoints.admin.core.product_download import ProductDownloadBase
from ....endpoints.admin.core.product_feature_set import ProductFeatureSetBase
from ....endpoints.admin.core.product_manufacturer import ProductManufacturerBase
from ....endpoints.admin.core.product_media import ProductMediaBase
from ....endpoints.admin.core.product_review import ProductReviewBase
from ....endpoints.admin.core.product_stream import ProductStreamBase
from ....endpoints.admin.core.property_group import PropertyGroupBase
from ....endpoints.admin.core.property_group_option import PropertyGroupOptionBase
from ....endpoints.admin.core.seo_url import SeoUrlBase
from ....endpoints.admin.core.tag import TagBase
from ....endpoints.admin.core.tax import TaxBase
from ...base_fields import Amount
from .unit import Unit


class Product(ProductBase["ProductEndpoint"]):
    _identifier = "product"

    downloads: list[ProductDownloadBase] | None = None
    parent: "Product | None" = None
    children: "list[Product] | None" = None
    delivery_time: DeliveryTimeBase | None = None
    tax: TaxBase | None = None
    manufacturer: ProductManufacturerBase | None = None
    unit: Unit | None = None
    cover: ProductMediaBase | None = None
    feature_set: ProductFeatureSetBase | None = None
    cms_page: CmsPageBase | None = None
    canonical_product: "Product | None" = None
    calculated_prices: list[Amount] | None
    calculated_price: Amount | None
    media: list[ProductMediaBase] | None
    cross_sellings: list[ProductCrossSellingBase] | None
    configurator_settings: list[ProductConfiguratorSettingBase] | None
    product_reviews: list[ProductReviewBase] | None
    main_categories: list[MainCategoryBase] | None
    seo_urls: list[SeoUrlBase] | None
    options: list[PropertyGroupOptionBase] | None
    properties: list[PropertyGroupBase] | None
    categories: list[CategoryBase] | None
    streams: list[ProductStreamBase] | None
    categories_ro: list[CategoryBase] | None
    tags: list[TagBase] | None


class ProductEndpoint(EndpointBase[Product]):
    name = "product"
    path = "/product"
    model_class = Product
    search_prefix = ""
    always_post = True
