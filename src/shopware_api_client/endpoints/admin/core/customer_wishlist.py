from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class CustomerWishlistBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer_wishlist"

    customer_id: IdField
    sales_channel_id: IdField
    custom_fields: dict[str, Any] | None = None


class CustomerWishlistRelations:
    products: ManyRelation["CustomerWishlistProduct"]
    customer: ForeignRelation["Customer"]
    sales_channel: ForeignRelation["SalesChannel"]


class CustomerWishlist(CustomerWishlistBase["CustomerWishlistEndpoint"], CustomerWishlistRelations):
    pass


class CustomerWishlistEndpoint(EndpointBase[CustomerWishlist]):
    name = "customer_wishlist"
    path = "/customer-wishlist"
    model_class = CustomerWishlist


from .customer import Customer  # noqa: E402
from .customer_wishlist_product import CustomerWishlistProduct  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
