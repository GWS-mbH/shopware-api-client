from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.product_stream_filter import ProductStreamFilterBase


class ProductStreamFilter(ProductStreamFilterBase, AdminModel["ProductStreamFilterEndpoint"]):
    product_stream: ForeignRelation["ProductStream"] = Field(default=...)
    parent: ForeignRelation["ProductStreamFilter"] = Field(default=...)
    queries: ManyRelation["ProductStreamFilter"] = Field(default=...)


class ProductStreamFilterEndpoint(AdminEndpoint[ProductStreamFilter]):
    name = "product_stream_filter"
    path = "/product-stream-filter"
    model_class = ProductStreamFilter


from .product_stream import ProductStream  # noqa: E402
