from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductSearchKeywordBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_search_keyword"

    version_id: IdField | None = None
    language_id: IdField
    product_id: IdField
    product_version_id: IdField | None = None
    keyword: str
    ranking: float


class ProductSearchKeywordRelations:
    product: ForeignRelation["Product"]
    language: ForeignRelation["Language"]


class ProductSearchKeyword(ProductSearchKeywordBase["ProductSearchKeywordEndpoint"], ProductSearchKeywordRelations):
    pass


class ProductSearchKeywordEndpoint(EndpointBase[ProductSearchKeyword]):
    name = "product_search_keyword"
    path = "/product-search-keyword"
    model_class = ProductSearchKeyword


from .language import Language  # noqa: E402
from .product import Product  # noqa: E402
