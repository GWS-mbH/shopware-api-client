from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import StateMachine, StateMachineState, User


class StateMachineHistoryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "state_machine_history"

    state_machine_id: IdField = Field(
        ..., serialization_alias="stateMachineId", validation_alias=AliasChoices("state_machine_id", "stateMachineId")
    )
    entity_name: str = Field(
        ..., serialization_alias="entityName", validation_alias=AliasChoices("entity_name", "entityName")
    )
    from_state_id: IdField = Field(
        ..., serialization_alias="fromStateId", validation_alias=AliasChoices("from_state_id", "fromStateId")
    )
    to_state_id: IdField = Field(
        ..., serialization_alias="toStateId", validation_alias=AliasChoices("to_state_id", "toStateId")
    )
    transition_action_name: str | None = Field(
        default=None,
        serialization_alias="transitionActionName",
        validation_alias=AliasChoices("transition_action_name", "transitionActionName"),
    )
    user_id: IdField | None = Field(
        default=None, serialization_alias="userId", validation_alias=AliasChoices("user_id", "userId")
    )
    entity_id: dict[str, Any] = Field(
        ..., serialization_alias="entityId", validation_alias=AliasChoices("entity_id", "entityId")
    )
    referenced_id: IdField | None = Field(
        default=None, serialization_alias="referencedId", validation_alias=AliasChoices("referenced_id", "referencedId")
    )
    referenced_version_id: IdField | None = Field(
        default=None,
        serialization_alias="referencedVersionId",
        validation_alias=AliasChoices("referenced_version_id", "referencedVersionId"),
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


class StateMachineHistoryRelations:
    state_machine: ClassVar[ForeignRelation["StateMachine"]] = ForeignRelation("StateMachine", "state_machine_id")
    from_state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "from_state_id")
    to_state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "to_state_id")
    user: ClassVar[ForeignRelation["User"]] = ForeignRelation("User", "user_id")


class StateMachineHistory(StateMachineHistoryBase["StateMachineHistoryEndpoint"], StateMachineHistoryRelations):
    pass


class StateMachineHistoryEndpoint(EndpointBase[StateMachineHistory]):
    name = "state_machine_history"
    path = "/state-machine-history"
    model_class = StateMachineHistory


registry.register_admin(StateMachineHistoryEndpoint)
