from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class AppScriptConditionBase(ApiModelBase[EndpointClass]):
    _identifier = "app_script_condition"

    identifier: str
    name: str
    active: bool
    group: str | None = None
    script: str | None = None
    config: list[dict[str, Any]] | None = None
    app_id: IdField
    translated: dict[str, Any] | None = None


class AppScriptConditionRelations:
    app: ForeignRelation["App"]
    rule_conditions: ManyRelation["RuleCondition"]


class AppScriptCondition(AppScriptConditionBase["AppScriptConditionEndpoint"], AppScriptConditionRelations):
    pass


class AppScriptConditionEndpoint(EndpointBase[AppScriptCondition]):
    name = "app_script_condition"
    path = "/app-script-condition"
    model_class = AppScriptCondition


from .app import App  # noqa: E402
from .rule_condition import RuleCondition  # noqa: E402
