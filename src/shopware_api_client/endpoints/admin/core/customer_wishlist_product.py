from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.customer_wishlist_product import CustomerWishlistProductBase


class CustomerWishlistProduct(CustomerWishlistProductBase, AdminModel["CustomerWishlistProductEndpoint"]):
    wishlist: ForeignRelation["CustomerWishlist"] = Field(default=...)
    product: ForeignRelation["Product"] = Field(default=...)


class CustomerWishlistProductEndpoint(AdminEndpoint[CustomerWishlistProduct]):
    name = "customer_wishlist_product"
    path = "/customer-wishlist-product"
    model_class = CustomerWishlistProduct


from .customer_wishlist import CustomerWishlist  # noqa: E402
from .product import Product  # noqa: E402
