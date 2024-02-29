from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField, Price
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import OrderDelivery, OrderLineItem


class OrderDeliveryPositionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_delivery_position"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    order_delivery_id: IdField = Field(
        ...,
        serialization_alias="orderDeliveryId",
        validation_alias=AliasChoices("order_delivery_id", "orderDeliveryId"),
    )
    order_delivery_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderDeliveryVersionId",
        validation_alias=AliasChoices("order_delivery_version_id", "orderDeliveryVersionId"),
    )
    order_line_item_id: IdField = Field(
        ...,
        serialization_alias="orderLineItemId",
        validation_alias=AliasChoices("order_line_item_id", "orderLineItemId"),
    )
    order_line_item_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderLineItemVersionId",
        validation_alias=AliasChoices("order_line_item_version_id", "orderLineItemVersionId"),
    )
    price: Price | None = None
    unit_price: float | None = Field(
        default=None, serialization_alias="unitPrice", validation_alias=AliasChoices("unit_price", "unitPrice")
    )
    total_price: float | None = Field(
        default=None, serialization_alias="totalPrice", validation_alias=AliasChoices("total_price", "totalPrice")
    )
    quantity: int | None = None
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


class OrderDeliveryPositionRelations:
    order_delivery: ClassVar[ForeignRelation["OrderDelivery"]] = ForeignRelation("OrderDelivery", "order_delivery_id")
    order_line_item: ClassVar[ForeignRelation["OrderLineItem"]] = ForeignRelation("OrderLineItem", "order_line_item_id")


class OrderDeliveryPosition(OrderDeliveryPositionBase["OrderDeliveryPositionEndpoint"], OrderDeliveryPositionRelations):
    pass


class OrderDeliveryPositionEndpoint(EndpointBase[OrderDeliveryPosition]):
    name = "order_delivery_position"
    path = "/order-delivery-position"
    model_class = OrderDeliveryPosition


registry.register_admin(OrderDeliveryPositionEndpoint)
