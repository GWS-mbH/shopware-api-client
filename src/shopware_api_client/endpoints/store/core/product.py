from shopware_api_client.base import StoreSearchEndpoint, EndpointMixin
from shopware_api_client.models.product import ProductBase


class Product(ProductBase, EndpointMixin["ProductEndpoint"]):
    calculated_price: "CalculatedPrice"
    calculated_prices: list["CalculatedPrice"]
    calculated_max_purchase: int | None = None
    calculated_cheapest_price: "CalculatedCheapestPrice | None" = None
    is_new: bool | None = None
    sorted_properties: list["PropertyGroup"] | None = None
    downloads: list["ProductDownload"] | None = None
    parent: "Product | None" = None
    children: list["Product"] | None = None
    delivery_time: "DeliveryTime | None" = None
    tax: "Tax | None" = None
    manufacturer: "ProductManufacturer | None" = None
    unit: "Unit | None" = None
    cover: "ProductMedia | None" = None
    cms_page: "CmsPage | None" = None
    canonical_product: "Product | None" = None
    media: list["ProductMedia"] | None = None
    cross_sellings: list["ProductCrossSelling"] | None = None
    configurator_settings: list["ProductConfiguratorSetting"] | None = None
    product_reviews: list["ProductReview"] | None = None
    main_categories: list["MainCategory"] | None = None
    seo_urls: list["SeoUrl"] | None = None
    options: list["PropertyGroupOption"] | None = None
    properties: list["PropertyGroupOption"] | None = None
    categories: list["Category"] | None = None
    streams: list["ProductStream"] | None = None
    categories_ro: list["Category"] | None = None
    tags: list["Tag"] | None = None
    seo_category: "Category | None" = None


class ProductEndpoint(StoreSearchEndpoint[Product]):
    model_class = Product
    path = "/search"


from shopware_api_client.structs.calculated_price import CalculatedPrice  # noqa: E402
from shopware_api_client.structs.calculated_cheapest_price import CalculatedCheapestPrice  # noqa: E402
from .category import Category  # noqa: E402
from .cms_page import CmsPage  # noqa: E402
from .delivery_time import DeliveryTime  # noqa: E402
from .main_category import MainCategory  # noqa: E402
from .product_configurator_setting import ProductConfiguratorSetting  # noqa: E402
from .product_cross_selling import ProductCrossSelling  # noqa: E402
from .product_download import ProductDownload  # noqa: E402
from .product_manufacturer import ProductManufacturer  # noqa: E402
from .product_media import ProductMedia  # noqa: E402
from .product_review import ProductReview  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
from .property_group import PropertyGroup  # noqa: E402
from .property_group_option import PropertyGroupOption  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .tag import Tag  # noqa: E402
from .tax import Tax  # noqa: E402
from .unit import Unit  # noqa: E402
