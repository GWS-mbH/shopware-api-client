from shopware_api_client.models.product_download import ProductDownloadBase


class ProductDownload(ProductDownloadBase):
    product: "Product | None" = None
    media: "Media | None" = None


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
