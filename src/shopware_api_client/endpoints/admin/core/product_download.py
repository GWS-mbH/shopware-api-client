from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductDownloadBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_download"

    version_id: IdField | None = None
    product_id: IdField
    product_version_id: IdField | None = None
    media_id: IdField
    position: int | None = None
    custom_fields: dict[str, Any] | None = None


class ProductDownloadRelations:
    product: ForeignRelation["Product"]
    media: ForeignRelation["Media"]


class ProductDownload(ProductDownloadBase["ProductDownloadEndpoint"], ProductDownloadRelations):
    pass


class ProductDownloadEndpoint(EndpointBase[ProductDownload]):
    name = "product_download"
    path = "/product-download"
    model_class = ProductDownload


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
