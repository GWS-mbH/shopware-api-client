from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.customer_wishlist import CustomerWishlistBase


class CustomerWishlist(CustomerWishlistBase, AdminModel["CustomerWishlistEndpoint"]):
    products: ManyRelation["CustomerWishlistProduct"] = Field(default=...)
    customer: ForeignRelation["Customer"] = Field(default=...)
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)


class CustomerWishlistEndpoint(AdminEndpoint[CustomerWishlist]):
    name = "customer_wishlist"
    path = "/customer-wishlist"
    model_class = CustomerWishlist


from .customer import Customer  # noqa: E402
from .customer_wishlist_product import CustomerWishlistProduct  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
