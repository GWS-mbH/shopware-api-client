from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class ProductCrossSellingBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_cross_selling"

    name: str
    position: int
    sort_by: str | None = None
    sort_direction: str | None = None
    type: str
    active: bool | None = None
    limit: int | None = None
    product_id: IdField
    product_version_id: IdField | None = None
    product_stream_id: IdField | None = None
    translated: dict[str, Any] | None = None


class ProductCrossSellingRelations:
    product: ForeignRelation["Product"]
    product_stream: ForeignRelation["ProductStream"]
    assigned_products: ManyRelation["ProductCrossSellingAssignedProducts"]


class ProductCrossSelling(ProductCrossSellingBase["ProductCrossSellingEndpoint"], ProductCrossSellingRelations):
    pass


class ProductCrossSellingEndpoint(EndpointBase[ProductCrossSelling]):
    name = "product_cross_selling"
    path = "/product-cross-selling"
    model_class = ProductCrossSelling


from .product import Product  # noqa: E402
from .product_cross_selling_assigned_products import ProductCrossSellingAssignedProducts  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
