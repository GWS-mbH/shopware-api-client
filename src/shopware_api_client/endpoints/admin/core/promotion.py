from typing import Any

from pydantic import AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ManyRelation


class PromotionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "promotion"

    name: str
    active: bool
    valid_from: AwareDatetime | None = None
    valid_until: AwareDatetime | None = None
    max_redemptions_global: int | None = None
    max_redemptions_per_customer: int | None = None
    priority: int
    exclusive: bool
    code: str | None = None
    use_codes: bool
    use_individual_codes: bool
    individual_code_pattern: str | None = None
    use_set_groups: bool
    customer_restriction: bool | None = None
    prevent_combination: bool
    order_count: int | None = Field(default=None, exclude=True)
    orders_per_customer_count: dict[str, Any] | None = Field(default=None, exclude=True)
    exclusion_ids: list[IdField] | None = None
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class PromotionRelations:
    sales_channels: ManyRelation["SalesChannel"]
    discounts: ManyRelation["PromotionDiscount"]
    persona_rules: ManyRelation["Rule"]
    persona_customers: ManyRelation["Customer"]
    order_rules: ManyRelation["Rule"]
    cart_rules: ManyRelation["Rule"]
    order_line_items: ManyRelation["OrderLineItem"]

    """
    Todo:
    setgroups[PromotionSetGroup], individual_codes[PromotionIndividualCode]
    """


class Promotion(PromotionBase["PromotionEndpoint"], PromotionRelations):
    pass


class PromotionEndpoint(EndpointBase[Promotion]):
    name = "promotion"
    path = "/promotion"
    model_class = Promotion


from .customer import Customer  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
from .promotion_discount import PromotionDiscount  # noqa: E402
from .rule import Rule  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
