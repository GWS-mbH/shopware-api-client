from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import App, RuleCondition


class AppScriptConditionBase(ApiModelBase[EndpointClass]):
    _identifier = "app_script_condition"

    identifier: str
    name: str
    active: bool
    group: str | None = None
    script: str | None = None
    config: dict[str, Any] | None = None
    app_id: IdField = Field(serialization_alias="appId", validation_alias=AliasChoices("app_id", "appId"))
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


class AppScriptConditionRelations:
    app: ClassVar[ForeignRelation["App"]] = ForeignRelation("App", "app")
    rule_conditions: ClassVar[ManyRelation["RuleCondition"]] = ManyRelation("RuleCondition", "ruleConditions")


class AppScriptCondition(AppScriptConditionBase["AppScriptConditionEndpoint"], AppScriptConditionRelations):
    pass


class AppScriptConditionEndpoint(EndpointBase[AppScriptCondition]):
    name = "app_script_condition"
    path = "/app-script-condition"
    model_class = AppScriptCondition


registry.register_admin(AppScriptConditionEndpoint)
