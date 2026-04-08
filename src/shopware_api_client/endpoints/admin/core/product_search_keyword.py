from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_search_keyword import ProductSearchKeywordBase


class ProductSearchKeyword(ProductSearchKeywordBase, AdminModel["ProductSearchKeywordEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    language: ForeignRelation["Language"] = Field(default=...)


class ProductSearchKeywordEndpoint(AdminEndpoint[ProductSearchKeyword]):
    name = "product_search_keyword"
    path = "/product-search-keyword"
    model_class = ProductSearchKeyword


from .language import Language  # noqa: E402
from .product import Product  # noqa: E402
