from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Customer, CustomerWishlistProduct, SalesChannel


class CustomerWishlistBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer_wishlist"

    customer_id: IdField = Field(
        ..., serialization_alias="customerId", validation_alias=AliasChoices("customer_id", "customerId")
    )
    sales_channel_id: IdField = Field(
        ..., serialization_alias="salesChannelId", validation_alias=AliasChoices("sales_channel_id", "salesChannelId")
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class CustomerWishlistRelations:
    products: ClassVar[ManyRelation["CustomerWishlistProduct"]] = ManyRelation("CustomerWishlistProduct", "products")
    customer: ClassVar[ForeignRelation["Customer"]] = ForeignRelation("Customer", "customer_id")
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")


class CustomerWishlist(CustomerWishlistBase["CustomerWishlistEndpoint"], CustomerWishlistRelations):
    pass


class CustomerWishlistEndpoint(EndpointBase[CustomerWishlist]):
    name = "customer_wishlist"
    path = "/customer-wishlist"
    model_class = CustomerWishlist


registry.register_admin(CustomerWishlistEndpoint)
