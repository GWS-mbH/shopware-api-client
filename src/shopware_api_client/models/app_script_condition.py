from typing import Annotated, Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class AppScriptConditionBase(ApiModelBase):
    _identifier = "app_script_condition"

    identifier: str
    name: str
    active: bool
    group: str | None = None
    script: str | None = None
    config: list[dict[str, Any]] | None = Field(default=None)
    app_id: Annotated[IdField, RefersTo("app")]
