from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Customer, OrderLineItem, PromotionDiscount, Rule, SalesChannel


class PromotionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "promotion"

    name: str
    active: bool
    valid_from: AwareDatetime | None = Field(
        default=None, serialization_alias="validFrom", validation_alias=AliasChoices("valid_from", "validFrom")
    )
    valid_until: AwareDatetime | None = Field(
        default=None, serialization_alias="validUntil", validation_alias=AliasChoices("valid_until", "validUntil")
    )
    max_redemptions_global: int | None = Field(
        default=None,
        serialization_alias="maxRedemptionsGlobal",
        validation_alias=AliasChoices("max_redemptions_global", "maxRedemptionsGlobal"),
    )
    max_redemptions_per_customer: int | None = Field(
        default=None,
        serialization_alias="maxRedemptionsPerCustomer",
        validation_alias=AliasChoices("max_redemptions_per_customer", "maxRedemptionsPerCustomer"),
    )
    priority: int
    exclusive: bool
    code: str | None = None
    use_codes: bool = Field(..., serialization_alias="useCodes", validation_alias=AliasChoices("use_codes", "useCodes"))
    use_individual_codes: bool = Field(
        ...,
        serialization_alias="useIndividualCodes",
        validation_alias=AliasChoices("use_individual_codes", "useIndividualCodes"),
    )
    individual_code_pattern: str | None = Field(
        default=None,
        serialization_alias="individualCodePattern",
        validation_alias=AliasChoices("individual_code_pattern", "individualCodePattern"),
    )
    use_set_groups: bool = Field(
        ..., serialization_alias="useSetGroups", validation_alias=AliasChoices("use_set_groups", "useSetGroups")
    )
    customer_restriction: bool | None = Field(
        default=None,
        serialization_alias="customerRestriction",
        validation_alias=AliasChoices("customer_restriction", "customerRestriction"),
    )
    prevent_combination: bool = Field(
        ...,
        serialization_alias="preventCombination",
        validation_alias=AliasChoices("prevent_combination", "preventCombination"),
    )
    order_count: int | None = Field(
        default=None,
        serialization_alias="orderCount",
        validation_alias=AliasChoices("order_count", "orderCount"),
        exclude=True,
    )
    orders_per_customer_count: dict[str, Any] | None = Field(
        default=None, serialization_alias="ordersPerCustomerCount", exclude=True
    )
    exclusion_ids: list[IdField] | None = Field(
        default=None, serialization_alias="exclusionIds", validation_alias=AliasChoices("exclusion_ids", "exclusionIds")
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
    translated: dict[str, Any] | None = None


class PromotionRelations:
    sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "salesChannels")
    discounts: ClassVar[ManyRelation["PromotionDiscount"]] = ManyRelation("PromotionDiscount", "discounts")
    persona_rules: ClassVar[ManyRelation["Rule"]] = ManyRelation("Rule", "personaRules")
    persona_customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "personaCustomers")
    order_rules: ClassVar[ManyRelation["Rule"]] = ManyRelation("Rule", "orderRules")
    cart_rules: ClassVar[ManyRelation["Rule"]] = ManyRelation("Rule", "cartRules")
    order_line_items: ClassVar[ManyRelation["OrderLineItem"]] = ManyRelation("OrderLineItem", "orderLineItems")

    """
    Todo:
    setgroups[PromotionSetGroup], individual_codes[PromotionIndividualCode]
    """


class Promotion(PromotionBase["PromotionEndpoint"], PromotionRelations):
    pass


class PromotionEndpoint(EndpointBase[Promotion]):
    name = "tag"
    path = "/tag"
    model_class = Promotion


registry.register_admin(PromotionEndpoint)
