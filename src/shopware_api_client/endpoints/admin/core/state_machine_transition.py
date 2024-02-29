from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import StateMachine, StateMachineState


class StateMachineTransitionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "state_machine_transition"

    action_name: str = Field(
        ..., serialization_alias="actionName", validation_alias=AliasChoices("action_name", "actionName")
    )
    state_machine_id: IdField = Field(
        ..., serialization_alias="stateMachineId", validation_alias=AliasChoices("state_machine_id", "stateMachineId")
    )
    from_state_id: IdField = Field(
        ..., serialization_alias="fromStateId", validation_alias=AliasChoices("from_state_id", "fromStateId")
    )
    to_state_id: IdField = Field(
        ..., serialization_alias="toStateId", validation_alias=AliasChoices("to_state_id", "toStateId")
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


class StateMachineTransitionRelations:
    state_machine: ClassVar[ForeignRelation["StateMachine"]] = ForeignRelation("StateMachine", "state_machine_id")
    from_state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "from_state_id")
    to_state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "to_state_id")


class StateMachineTransition(
    StateMachineTransitionBase["StateMachineTransitionEndpoint"], StateMachineTransitionRelations
):
    pass


class StateMachineTransitionEndpoint(EndpointBase[StateMachineTransition]):
    name = "state_machine_transition"
    path = "/state-machine-transition"
    model_class = StateMachineTransition


registry.register_admin(StateMachineTransitionEndpoint)
