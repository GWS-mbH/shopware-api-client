from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class ProductSearchKeyword(ApiModelBase):
    _identifier: str = "product_search_keyword"

    version_id: IdField | None = None
    language_id: IdField
    product_id: IdField
    product_version_id: IdField | None = None
    keyword: str
    ranking: float
