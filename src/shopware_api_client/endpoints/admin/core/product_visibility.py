from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductVisibilityBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_visibility"

    product_id: IdField
    product_version_id: IdField | None = None
    sales_channel_id: IdField
    visibility: int


class ProductVisibilityRelations:
    sales_channel: ForeignRelation["SalesChannel"]
    product: ForeignRelation["Product"]


class ProductVisibility(ProductVisibilityBase["ProductVisibilityEndpoint"], ProductVisibilityRelations):
    pass


class ProductVisibilityEndpoint(EndpointBase[ProductVisibility]):
    name = "product_visibility"
    path = "/product-visibility"
    model_class = ProductVisibility


from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
