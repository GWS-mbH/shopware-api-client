from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import DeliveryTime, Media, OrderDelivery, Rule, SalesChannel, Tag, Tax


class ShippingMethodBase(ApiModelBase[EndpointClass]):
    _identifier: str = "shipping_method"

    name: str
    active: bool | None = None
    position: int | None = None
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    availability_rule_id: IdField = Field(
        ...,
        serialization_alias="availabilityRuleId",
        validation_alias=AliasChoices("availability_rule_id", "availabilityRuleId"),
    )
    media_id: IdField | None = Field(
        default=None, serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId")
    )
    delivery_time_id: IdField = Field(
        ..., serialization_alias="deliveryTimeId", validation_alias=AliasChoices("delivery_time_id", "deliveryTimeId")
    )
    tax_type: str = Field(..., serialization_alias="taxType", validation_alias=AliasChoices("tax_type", "taxType"))
    tax_id: IdField | None = Field(
        default=None, serialization_alias="taxId", validation_alias=AliasChoices("tax_id", "taxId")
    )
    description: str | None = None
    tracking_url: str | None = Field(
        default=None, serialization_alias="trackingUrl", validation_alias=AliasChoices("tracking_url", "trackingUrl")
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


class ShippingMethodRelations:
    delivery_time: ClassVar[ForeignRelation["DeliveryTime"]] = ForeignRelation("DeliveryTime", "delivery_time_id")
    availability_rule: ClassVar[ForeignRelation["Rule"]] = ForeignRelation("Rule", "availability_rule_id")
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")
    tags: ClassVar[ManyRelation["Tag"]] = ManyRelation("Tag", "tags")
    order_deliveries: ClassVar[ManyRelation["OrderDelivery"]] = ManyRelation("OrderDelivery", "orderDeliveries")
    sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "salesChannels")
    sales_channel_default_assignments: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "salesChannelDefaultAssignments"
    )
    tax: ClassVar[ForeignRelation["Tax"]] = ForeignRelation("Tax", "tax_id")

    """
    Todo:
    prices[ShippingMethodPrice], app_shipping_method[AppShippingMethod]
    """


class ShippingMethod(ShippingMethodBase["ShippingMethodEndpoint"], ShippingMethodRelations):
    pass


class ShippingMethodEndpoint(EndpointBase[ShippingMethod]):
    name = "shipping_method"
    path = "/shipping-method"
    model_class = ShippingMethod


registry.register_admin(ShippingMethodEndpoint)
