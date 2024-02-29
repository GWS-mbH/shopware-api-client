from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import CustomerWishlist, Product


class CustomerWishlistProductBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer_wishlist_product"

    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    wishlist_id: IdField = Field(
        ..., serialization_alias="wishlistId", validation_alias=AliasChoices("wishlist_id", "wishlistId")
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


class CustomerWishlistProductRelations:
    wishlist: ClassVar[ForeignRelation["CustomerWishlist"]] = ForeignRelation("CustomerWishlist", "wishlist_id")
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")


class CustomerWishlistProduct(
    CustomerWishlistProductBase["CustomerWishlistProductEndpoint"], CustomerWishlistProductRelations
):
    pass


class CustomerWishlistProductEndpoint(EndpointBase[CustomerWishlistProduct]):
    name = "customer_wishlist_product"
    path = "/customer-wishlist-product"
    model_class = CustomerWishlistProduct


registry.register_admin(CustomerWishlistProductEndpoint)
