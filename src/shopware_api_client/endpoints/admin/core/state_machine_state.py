from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import (
        Order,
        OrderDelivery,
        OrderTransaction,
        OrderTransactionCapture,
        OrderTransactionCaptureRefund,
        StateMachine,
        StateMachineHistory,
        StateMachineTransition,
    )


class StateMachineStateBase(ApiModelBase[EndpointClass]):
    _identifier: str = "state_machine_state"

    technical_name: str = Field(
        ..., serialization_alias="technicalName", validation_alias=AliasChoices("technical_name", "technicalName")
    )
    name: str
    state_machine_id: IdField = Field(
        ..., serialization_alias="stateMachineId", validation_alias=AliasChoices("state_machine_id", "stateMachineId")
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


class StateMachineStateRelations:
    state_machine: ClassVar[ForeignRelation["StateMachine"]] = ForeignRelation("StateMachine", "state_machine_id")
    from_state_machine_transitions: ClassVar[ManyRelation["StateMachineTransition"]] = ManyRelation(
        "StateMachineTransition", "fromStateMachineTransitions"
    )
    to_state_machine_transitions: ClassVar[ManyRelation["StateMachineTransition"]] = ManyRelation(
        "StateMachineTransition", "toStateMachineTransitions"
    )
    order_transactions: ClassVar[ManyRelation["OrderTransaction"]] = ManyRelation(
        "OrderTransaction", "orderTransactions"
    )
    order_deliveries: ClassVar[ManyRelation["OrderDelivery"]] = ManyRelation("OrderDelivery", "orderDeliveries")
    orders: ClassVar[ManyRelation["Order"]] = ManyRelation("Order", "orders")
    order_transaction_captures: ClassVar[ManyRelation["OrderTransactionCapture"]] = ManyRelation(
        "OrderTransactionCapture", "orderTransactionCaptures"
    )
    order_transaction_capture_refunds: ClassVar[ManyRelation["OrderTransactionCaptureRefund"]] = ManyRelation(
        "OrderTransactionCaptureRefund", "orderTransactionCaptureRefunds"
    )
    to_state_machine_history_entries: ClassVar[ManyRelation["StateMachineHistory"]] = ManyRelation(
        "StateMachineHistory", "toStateMachineHistoryEntries"
    )
    from_state_machine_history_entries: ClassVar[ManyRelation["StateMachineHistory"]] = ManyRelation(
        "StateMachineHistory", "fromStateMachineHistoryEntries"
    )


class StateMachineState(StateMachineStateBase["StateMachineStateEndpoint"], StateMachineStateRelations):
    pass


class StateMachineStateEndpoint(EndpointBase[StateMachineState]):
    name = "state_machine_state"
    path = "/state-machine-state"
    model_class = StateMachineState


registry.register_admin(StateMachineStateEndpoint)
