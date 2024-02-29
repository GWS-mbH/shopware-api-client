from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Customer, Media, OrderTransaction, Rule, SalesChannel


class PaymentMethodBase(ApiModelBase[EndpointClass]):
    _identifier: str = "payment_method"

    plugin_id: IdField | None = Field(
        default=None, serialization_alias="pluginId", validation_alias=AliasChoices("plugin_id", "pluginId")
    )
    handler_identifier: str | None = Field(
        default=None,
        serialization_alias="handlerIdentifier",
        validation_alias=AliasChoices("handler_identifier", "handlerIdentifier"),
    )
    name: str
    distinguishable_name: str | None = Field(
        default=None,
        serialization_alias="distinguishableName",
        validation_alias=AliasChoices("distinguishable_name", "distinguishableName"),
        exclude=True,
    )
    description: str | None = None
    position: int | None = None
    active: bool | None = None
    after_order_enabled: bool | None = Field(
        default=None,
        serialization_alias="afterOrderEnabled",
        validation_alias=AliasChoices("after_order_enabled", "afterOrderEnabled"),
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    availability_rule_id: IdField | None = Field(
        default=None,
        serialization_alias="availabilityRuleId",
        validation_alias=AliasChoices("availability_rule_id", "availabilityRuleId"),
    )
    media_id: IdField | None = Field(
        default=None, serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId")
    )
    formatted_handler_identifier: str | None = Field(
        None,
        alias="formattedHandlerIdentifier",
        description="Runtime field, cannot be used as part of the criteria.",
        exclude=True,
    )
    synchronous: bool | None = Field(
        None, description="Runtime field, cannot be used as part of the criteria.", exclude=True
    )
    asynchronous: bool | None = Field(
        None, description="Runtime field, cannot be used as part of the criteria.", exclude=True
    )
    prepared: bool | None = Field(
        None, description="Runtime field, cannot be used as part of the criteria.", exclude=True
    )
    refundable: bool | None = Field(
        None, description="Runtime field, cannot be used as part of the criteria.", exclude=True
    )
    recurring: bool | None = Field(
        None, description="Runtime field, cannot be used as part of the criteria.", exclude=True
    )
    short_name: str | None = Field(
        None,
        alias="shortName",
        description="Runtime field, cannot be used as part of the criteria.",
    )
    technical_name: str | None = Field(
        default=None,
        serialization_alias="technicalName",
        validation_alias=AliasChoices("technical_name", "technicalName"),
        exclude=True,
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


class PaymentMethodRelations:
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")
    availability_rule: ClassVar[ForeignRelation["Rule"]] = ForeignRelation("Rule", "availability_rule_id")
    sales_channel_default_assignments: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "salesChannelDefaultAssignments"
    )
    customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "customers")
    order_transactions: ClassVar[ManyRelation["OrderTransaction"]] = ManyRelation(
        "OrderTransaction", "orderTransactions"
    )
    sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "salesChannels")

    """
    Todo:
    plugin[Plugin], orderTransactions, app_payment_method[AppPaymentMethod]
    """


class PaymentMethod(PaymentMethodBase["PaymentMethodEndpoint"], PaymentMethodRelations):
    pass


class PaymentMethodEndpoint(EndpointBase[PaymentMethod]):
    name = "payment_method"
    path = "/payment-method"
    model_class = PaymentMethod


registry.register_admin(PaymentMethodEndpoint)
