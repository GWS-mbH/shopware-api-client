from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import StateMachineHistory, StateMachineState, StateMachineTransition


class StateMachineBase(ApiModelBase[EndpointClass]):
    _identifier: str = "state_machine"

    technical_name: str = Field(
        ..., serialization_alias="technicalName", validation_alias=AliasChoices("technical_name", "technicalName")
    )
    name: str
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    initial_state_id: IdField | None = Field(
        default=None,
        serialization_alias="initialStateId",
        validation_alias=AliasChoices("initial_state_id", "initialStateId"),
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


class StateMachineRelations:
    states: ClassVar[ManyRelation["StateMachineState"]] = ManyRelation("StateMachineState", "states")
    transitions: ClassVar[ManyRelation["StateMachineTransition"]] = ManyRelation(
        "StateMachineTransition", "transitions"
    )
    history_entries: ClassVar[ManyRelation["StateMachineHistory"]] = ManyRelation(
        "StateMachineHistory", "historyEntries"
    )


class StateMachine(StateMachineBase["StateMachineEndpoint"], StateMachineRelations):
    pass


class StateMachineEndpoint(EndpointBase[StateMachine]):
    name = "state_machine"
    path = "/state-machine"
    model_class = StateMachine


registry.register_admin(StateMachineEndpoint)
