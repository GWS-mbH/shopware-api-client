from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.category import CategoryBase


class Category(CategoryBase, AdminModel["CategoryEndpoint"]):
    parent: ForeignRelation["Category"] = Field(default=...)
    children: ManyRelation["Category"] = Field(default=...)
    media: ForeignRelation["Media"] = Field(default=...)
    products: ManyRelation["Product"] = Field(default=...)
    nested_products: ManyRelation["Product"] = Field(default=...)
    tags: ManyRelation["Tag"] = Field(default=...)
    cms_page: ForeignRelation["CmsPage"] = Field(default=...)
    product_stream: ForeignRelation["ProductStream"] = Field(default=...)
    navigation_sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    footer_sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    service_sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    main_categories: ManyRelation["MainCategory"] = Field(default=...)
    seo_urls: ManyRelation["SeoUrl"] = Field(default=...)


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
