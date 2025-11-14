from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.category import CategoryBase


class Category(CategoryBase, AdminModel["CategoryEndpoint"]):
    parent: ForeignRelation["Category"]
    children: ManyRelation["Category"]
    media: ForeignRelation["Media"]
    products: ManyRelation["Product"]
    nested_products: ManyRelation["Product"]
    tags: ManyRelation["Tag"]
    cms_page: ForeignRelation["CmsPage"]
    product_stream: ForeignRelation["ProductStream"]
    navigation_sales_channels: ManyRelation["SalesChannel"]
    footer_sales_channels: ManyRelation["SalesChannel"]
    service_sales_channels: ManyRelation["SalesChannel"]
    main_categories: ManyRelation["MainCategory"]
    seo_urls: ManyRelation["SeoUrl"]


class CategoryEndpoint(AdminEndpoint[Category]):
    name = "category"
    path = "/category"
    model_class = Category


from .cms_page import CmsPage  # noqa: E402
from .main_category import MainCategory  # noqa: E402
from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .tag import Tag  # noqa: E402
