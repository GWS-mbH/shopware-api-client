from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductCrossSellingAssignedProductsBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_cross_selling_assigned_products"

    cross_selling_id: IdField
    product_id: IdField
    product_version_id: IdField | None = None
    position: int | None = None


class ProductCrossSellingAssignedProductsRelations:
    product: ForeignRelation["Product"]
    cross_selling: ForeignRelation["ProductCrossSelling"]


class ProductCrossSellingAssignedProducts(
    ProductCrossSellingAssignedProductsBase["ProductCrossSellingAssignedProductsEndpoint"],
    ProductCrossSellingAssignedProductsRelations,
):
    pass


class ProductCrossSellingAssignedProductsEndpoint(EndpointBase[ProductCrossSellingAssignedProducts]):
    name = "product_cross_selling_assigned_products"
    path = "/product-cross-selling-assigned-products"
    model_class = ProductCrossSellingAssignedProducts


from .product import Product  # noqa: E402
from .product_cross_selling import ProductCrossSelling  # noqa: E402
