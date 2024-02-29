from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Order, OrderTransactionCapture, PaymentMethod, StateMachineState


class OrderTransactionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_transaction"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    order_id: IdField = Field(..., serialization_alias="orderId", validation_alias=AliasChoices("order_id", "orderId"))
    order_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderVersionId",
        validation_alias=AliasChoices("order_version_id", "orderVersionId"),
    )
    payment_method_id: IdField = Field(
        ...,
        serialization_alias="paymentMethodId",
        validation_alias=AliasChoices("payment_method_id", "paymentMethodId"),
    )
    amount: Amount
    state_id: IdField = Field(..., serialization_alias="stateId", validation_alias=AliasChoices("state_id", "stateId"))
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


class OrderTransactionRelations:
    state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "state_id")
    order: ClassVar[ForeignRelation["Order"]] = ForeignRelation("Order", "order_id")
    payment_method: ClassVar[ForeignRelation["PaymentMethod"]] = ForeignRelation("PaymentMethod", "payment_method_id")
    captures: ClassVar[ManyRelation["OrderTransactionCapture"]] = ManyRelation("OrderTransactionCapture", "captures")


class OrderTransaction(OrderTransactionBase["OrderTransactionEndpoint"], OrderTransactionRelations):
    pass


class OrderTransactionEndpoint(EndpointBase[OrderTransaction]):
    name = "order_transaction"
    path = "/order-transaction"
    model_class = OrderTransaction


registry.register_admin(OrderTransactionEndpoint)
