from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class ProductManufacturerBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_manufacturer"

    version_id: IdField | None = None
    media_id: IdField | None = None
    link: str | None = None
    name: str
    description: str | None = None
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class ProductManufacturerRelations:
    media: ForeignRelation["Media"]
    products: ManyRelation["Product"]


class ProductManufacturer(ProductManufacturerBase["ProductManufacturerEndpoint"], ProductManufacturerRelations):
    pass


class ProductManufacturerEndpoint(EndpointBase[ProductManufacturer]):
    name = "product_manufacturer"
    path = "/product-manufacturer"
    model_class = ProductManufacturer


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
