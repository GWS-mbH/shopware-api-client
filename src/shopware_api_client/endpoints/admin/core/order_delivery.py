from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Order, OrderAddress, OrderDeliveryPosition, ShippingMethod, StateMachineState


class OrderDeliveryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_delivery"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    order_id: IdField = Field(..., serialization_alias="orderId", validation_alias=AliasChoices("order_id", "orderId"))
    order_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderVersionId",
        validation_alias=AliasChoices("order_version_id", "orderVersionId"),
    )
    shipping_order_address_id: IdField = Field(
        ...,
        serialization_alias="shippingOrderAddressId",
        validation_alias=AliasChoices("shipping_order_address_id", "shippingOrderAddressId"),
    )
    shipping_order_address_version_id: IdField | None = Field(
        default=None, serialization_alias="shippingOrderAddressVersionId"
    )
    shipping_method_id: IdField = Field(
        ...,
        serialization_alias="shippingMethodId",
        validation_alias=AliasChoices("shipping_method_id", "shippingMethodId"),
    )
    state_id: IdField = Field(..., serialization_alias="stateId", validation_alias=AliasChoices("state_id", "stateId"))
    tracking_codes: list[str] = Field(
        ..., serialization_alias="trackingCodes", validation_alias=AliasChoices("tracking_codes", "trackingCodes")
    )
    shipping_date_earliest: AwareDatetime = Field(
        ...,
        serialization_alias="shippingDateEarliest",
        validation_alias=AliasChoices("shipping_date_earliest", "shippingDateEarliest"),
    )
    shipping_date_latest: AwareDatetime = Field(
        ...,
        serialization_alias="shippingDateLatest",
        validation_alias=AliasChoices("shipping_date_latest", "shippingDateLatest"),
    )
    shipping_costs: Amount | None = Field(
        default=None,
        serialization_alias="shippingCosts",
        validation_alias=AliasChoices("shipping_costs", "shippingCosts"),
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


class OrderDeliveryRelations:
    state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "state_id")
    order: ClassVar[ForeignRelation["Order"]] = ForeignRelation("Order", "order_id")
    shipping_order_address: ClassVar[ForeignRelation["OrderAddress"]] = ForeignRelation(
        "OrderAddress", "shipping_order_address_id"
    )
    shipping_method: ClassVar[ForeignRelation["ShippingMethod"]] = ForeignRelation(
        "ShippingMethod", "shipping_method_id"
    )
    positions: ClassVar[ManyRelation["OrderDeliveryPosition"]] = ManyRelation("OrderDeliveryPosition", "positions")


class OrderDelivery(OrderDeliveryBase["OrderDeliveryEndpoint"], OrderDeliveryRelations):
    pass


class OrderDeliveryEndpoint(EndpointBase[OrderDelivery]):
    name = "order_delivery"
    path = "/order-delivery"
    model_class = OrderDelivery


registry.register_admin(OrderDeliveryEndpoint)
