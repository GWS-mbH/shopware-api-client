from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.product_media import ProductMediaBase


class ProductMedia(ProductMediaBase, AdminModel["ProductMediaEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    media: ForeignRelation["Media"] = Field(default=...)
    cover_products: ManyRelation["Product"] = Field(default=...)


class ProductMediaEndpoint(AdminEndpoint[ProductMedia]):
    name = "product_media"
    path = "/product-media"
    model_class = ProductMedia


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
