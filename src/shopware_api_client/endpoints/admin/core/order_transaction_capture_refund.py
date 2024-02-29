from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import OrderTransactionCapture, OrderTransactionCaptureRefundPosition, StateMachineState


class OrderTransactionCaptureRefundBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_transaction_capture_refund"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    capture_id: IdField = Field(
        ..., serialization_alias="captureId", validation_alias=AliasChoices("capture_id", "captureId")
    )
    capture_version_id: IdField | None = Field(
        default=None,
        serialization_alias="captureVersionId",
        validation_alias=AliasChoices("capture_version_id", "captureVersionId"),
    )
    state_id: IdField = Field(..., serialization_alias="stateId", validation_alias=AliasChoices("state_id", "stateId"))
    external_reference: str | None = Field(
        default=None,
        serialization_alias="externalReference",
        validation_alias=AliasChoices("external_reference", "externalReference"),
    )
    reason: str | None = None
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


class OrderTransactionCaptureRefundRelations:
    state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "state_id")
    capture: ClassVar[ForeignRelation["OrderTransactionCapture"]] = ForeignRelation(
        "OrderTransactionCapture", "capture_id"
    )
    positions: ClassVar[ManyRelation["OrderTransactionCaptureRefundPosition"]] = ManyRelation(
        "OrderTransactionCaptureRefundPosition", "positions"
    )


class OrderTransactionCaptureRefund(
    OrderTransactionCaptureRefundBase["OrderTransactionCaptureRefundEndpoint"], OrderTransactionCaptureRefundRelations
):
    pass


class OrderTransactionCaptureRefundEndpoint(EndpointBase[OrderTransactionCaptureRefund]):
    name = "order_transaction_capture_refund"
    path = "/order-transaction-capture-refund"
    model_class = OrderTransactionCaptureRefund


registry.register_admin(OrderTransactionCaptureRefundEndpoint)
