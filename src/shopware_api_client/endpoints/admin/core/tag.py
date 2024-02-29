from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Category, Customer, LandingPage, Media, Order, Product, Rule, ShippingMethod


class TagBase(ApiModelBase[EndpointClass]):
    _identifier: str = "tag"

    name: str
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class TagRelations:
    products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "products")
    media: ClassVar[ManyRelation["Media"]] = ManyRelation("Media", "media")
    categories: ClassVar[ManyRelation["Category"]] = ManyRelation("Category", "categories")
    customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "customers")
    orders: ClassVar[ManyRelation["Order"]] = ManyRelation("Order", "orders")
    shipping_methods: ClassVar[ManyRelation["ShippingMethod"]] = ManyRelation("ShippingMethod", "shippingMethods")
    landing_pages: ClassVar[ManyRelation["LandingPage"]] = ManyRelation("LandingPage", "landingPages")
    rules: ClassVar[ManyRelation["Rule"]] = ManyRelation("Rule", "rules")

    """
    Todo:
    newsletter_recipients[NewsletterRecipient]
    """


class Tag(TagBase["TagEndpoint"], TagRelations):
    pass


class TagEndpoint(EndpointBase[Tag]):
    name = "tag"
    path = "/tag"
    model_class = Tag


registry.register_admin(TagEndpoint)
