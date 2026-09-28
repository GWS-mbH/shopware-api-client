from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductSearchKeywordBase(ApiModelBase):
    _identifier: str = "product_search_keyword"

    language_id: Annotated[IdField, RefersTo("language")]
    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    keyword: str
    ranking: float
