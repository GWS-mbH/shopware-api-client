from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.promotion import PromotionBase


class Promotion(PromotionBase, AdminModel["PromotionEndpoint"]):
    sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    discounts: ManyRelation["PromotionDiscount"] = Field(default=...)
    persona_rules: ManyRelation["Rule"] = Field(default=...)
    persona_customers: ManyRelation["Customer"] = Field(default=...)
    order_rules: ManyRelation["Rule"] = Field(default=...)
    cart_rules: ManyRelation["Rule"] = Field(default=...)
    order_line_items: ManyRelation["OrderLineItem"] = Field(default=...)

    """
    Todo:
    setgroups[PromotionSetGroup], individual_codes[PromotionIndividualCode]
    """


class PromotionEndpoint(AdminEndpoint[Promotion]):
    name = "promotion"
    path = "/promotion"
    model_class = Promotion


from .customer import Customer  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
from .promotion_discount import PromotionDiscount  # noqa: E402
from .rule import Rule  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
