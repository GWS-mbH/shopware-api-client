from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class ProductMediaBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_media"

    version_id: IdField | None = None
    product_id: IdField
    product_version_id: IdField | None = None
    media_id: IdField
    position: int | None = None
    custom_fields: dict[str, Any] | None = None


class ProductMediaRelations:
    product: ForeignRelation["Product"]
    media: ForeignRelation["Media"]
    cover_products: ManyRelation["Product"]


class ProductMedia(ProductMediaBase["ProductMediaEndpoint"], ProductMediaRelations):
    pass


class ProductMediaEndpoint(EndpointBase[ProductMedia]):
    name = "product_media"
    path = "/product-media"
    model_class = ProductMedia


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
