from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import OrderTransaction, OrderTransactionCaptureRefund, StateMachineState


class OrderTransactionCaptureBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_transaction_capture"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    order_transaction_id: IdField = Field(
        ...,
        serialization_alias="orderTransactionId",
        validation_alias=AliasChoices("order_transaction_id", "orderTransactionId"),
    )
    order_transaction_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderTransactionVersionId",
        validation_alias=AliasChoices("order_transaction_version_id", "orderTransactionVersionId"),
    )
    state_id: IdField = Field(..., serialization_alias="stateId", validation_alias=AliasChoices("state_id", "stateId"))
    external_reference: str | None = Field(
        default=None,
        serialization_alias="externalReference",
        validation_alias=AliasChoices("external_reference", "externalReference"),
    )
    amount: Amount
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


class OrderTransactionCaptureRelations:
    state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "state_id")
    order_transaction: ClassVar[ForeignRelation["OrderTransaction"]] = ForeignRelation(
        "OrderTransaction", "order_transaction_id"
    )
    refunds: ClassVar[ManyRelation["OrderTransactionCaptureRefund"]] = ManyRelation(
        "OrderTransactionCaptureRefund", "refunds"
    )


class OrderTransactionCapture(
    OrderTransactionCaptureBase["OrderTransactionCaptureEndpoint"], OrderTransactionCaptureRelations
):
    pass


class OrderTransactionCaptureEndpoint(EndpointBase[OrderTransactionCapture]):
    name = "order_transaction_capture"
    path = "/order-transaction-capture"
    model_class = OrderTransactionCapture


registry.register_admin(OrderTransactionCaptureEndpoint)
