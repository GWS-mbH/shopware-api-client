from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class ProductStreamBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_stream"

    api_filter: dict[str, Any] | None = Field(default=None, exclude=True)
    invalid: bool | None = Field(default=None, exclude=True)
    name: str
    description: str | None = None
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class ProductStreamRelations:
    product_cross_sellings: ManyRelation["ProductCrossSelling"]
    product_exports: ManyRelation["ProductExport"]
    categories: ManyRelation["Category"]

    """
    Todo:
    filters[ProductStreamFilter]
    """


class ProductStream(ProductStreamBase["ProductStreamEndpoint"], ProductStreamRelations):
    pass


class ProductStreamEndpoint(EndpointBase[ProductStream]):
    name = "product_stream"
    path = "/product-stream"
    model_class = ProductStream


from .category import Category  # noqa: E402
from .product_cross_selling import ProductCrossSelling  # noqa: E402
from .product_export import ProductExport  # noqa: E402
