from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class TaxBase(ApiModelBase[EndpointClass]):
    _identifier: str = "tax"

    tax_rate: float
    name: str
    position: int = Field(..., description="Added since version: 6.4.0.0.")
    custom_fields: dict[str, Any] | None = None


class TaxRelations:
    products: ManyRelation["Product"]
    rules: ManyRelation["Rule"]
    shipping_methods: ManyRelation["ShippingMethod"]


class Tax(TaxBase["TaxEndpoint"], TaxRelations):
    pass


class TaxEndpoint(EndpointBase[Tax]):
    name = "tax"
    path = "/tax"
    model_class = Tax


from .product import Product  # noqa: E402
from .rule import Rule  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
