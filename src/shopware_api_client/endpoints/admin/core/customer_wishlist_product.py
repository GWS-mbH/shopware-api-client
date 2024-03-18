from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class CustomerWishlistProductBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer_wishlist_product"

    product_id: IdField
    product_version_id: IdField | None = None
    wishlist_id: IdField


class CustomerWishlistProductRelations:
    wishlist: ForeignRelation["CustomerWishlist"]
    product: ForeignRelation["Product"]


class CustomerWishlistProduct(
    CustomerWishlistProductBase["CustomerWishlistProductEndpoint"], CustomerWishlistProductRelations
):
    pass


class CustomerWishlistProductEndpoint(EndpointBase[CustomerWishlistProduct]):
    name = "customer_wishlist_product"
    path = "/customer-wishlist-product"
    model_class = CustomerWishlistProduct


from .customer_wishlist import CustomerWishlist  # noqa: E402
from .product import Product  # noqa: E402
