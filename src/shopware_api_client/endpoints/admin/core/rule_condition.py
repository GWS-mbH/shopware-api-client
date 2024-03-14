from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import AppScriptCondition, Rule


class RuleConditionBase(ApiModelBase[EndpointClass]):
    _identifier = "rule_condition"

    type: str
    rule_id: IdField = Field(serialization_alias="ruleId", validation_alias=AliasChoices("rule_id", "ruleId"))
    script_id: IdField | None = Field(
        default=None, serialization_alias="scriptId", validation_alias=AliasChoices("script_id", "scriptId")
    )
    parent_id: IdField | None = Field(
        default=None, serialization_alias="parentId", validation_alias=AliasChoices("parent_id", "parentId")
    )
    value: dict[str, Any] | None = None
    position: int | None = None
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


class RuleConditionRelations:
    rule: ClassVar[ForeignRelation["Rule"]] = ForeignRelation("Rule", "rule")
    app_script_condition: ClassVar[ForeignRelation["AppScriptCondition"]] = ForeignRelation(
        "AppScriptCondition", "appScriptCondition"
    )
    parent: ClassVar[ForeignRelation["RuleCondition"]] = ForeignRelation("RuleCondition", "parent")
    children: ClassVar[ManyRelation["RuleCondition"]] = ManyRelation("RuleCondition", "children")


class RuleCondition(RuleConditionBase["RuleConditionEndpoint"], RuleConditionRelations):
    pass


class RuleConditionEndpoint(EndpointBase[RuleCondition]):
    name = "rule_condition"
    path = "/rule-condition"
    model_class = RuleCondition


registry.register_admin(RuleConditionEndpoint)
