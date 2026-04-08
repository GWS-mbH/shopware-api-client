from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_download import ProductDownloadBase


class ProductDownload(ProductDownloadBase, AdminModel["ProductDownloadEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    media: ForeignRelation["Media"] = Field(default=...)


class ProductDownloadEndpoint(AdminEndpoint[ProductDownload]):
    name = "product_download"
    path = "/product-download"
    model_class = ProductDownload


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
