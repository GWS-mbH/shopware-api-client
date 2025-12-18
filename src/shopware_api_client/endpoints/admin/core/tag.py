from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.tag import TagBase


class Tag(TagBase, AdminModel["TagEndpoint"]):
    products: ManyRelation["Product"] = Field(default=...)
    media: ManyRelation["Media"] = Field(default=...)
    categories: ManyRelation["Category"] = Field(default=...)
    customers: ManyRelation["Customer"] = Field(default=...)
    orders: ManyRelation["Order"] = Field(default=...)
    shipping_methods: ManyRelation["ShippingMethod"] = Field(default=...)
    landing_pages: ManyRelation["LandingPage"] = Field(default=...)
    rules: ManyRelation["Rule"] = Field(default=...)

    """
    Todo:
    newsletter_recipients[NewsletterRecipient]
    """


class TagEndpoint(AdminEndpoint[Tag]):
    name = "tag"
    path = "/tag"
    model_class = Tag


from .category import Category  # noqa: E402
from .customer import Customer  # noqa: E402
from .landing_page import LandingPage  # noqa: E402
from .media import Media  # noqa: E402
from .order import Order  # noqa: E402
from .product import Product  # noqa: E402
from .rule import Rule  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
