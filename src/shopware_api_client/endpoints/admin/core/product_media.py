from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.product_media import ProductMedia as ProductMediaBase


class ProductMedia(ProductMediaBase, AdminModel["ProductMediaEndpoint"]):
    product: ForeignRelation["Product"]
    media: ForeignRelation["Media"]
    cover_products: ManyRelation["Product"]


class ProductMediaEndpoint(AdminEndpoint[ProductMedia]):
    name = "product_media"
    path = "/product-media"
    model_class = ProductMedia


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
