from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductPriceBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_price"

    version_id: IdField | None = None
    product_id: IdField
    product_version_id: IdField | None = None
    rule_id: IdField
    price: dict[str, Any]
    quantity_start: int
    quantity_end: int | None = None
    custom_fields: dict[str, Any] | None = None


class ProductPriceRelations:
    product: ForeignRelation["Product"]
    rule: ForeignRelation["Rule"]


class ProductPrice(ProductPriceBase["ProductPriceEndpoint"], ProductPriceRelations):
    pass


class ProductPriceEndpoint(EndpointBase[ProductPrice]):
    name = "product_price"
    path = "/product-price"
    model_class = ProductPrice


from .product import Product  # noqa: E402
from .rule import Rule  # noqa: E402
