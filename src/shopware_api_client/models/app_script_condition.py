from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class AppScriptConditionBase(ApiModelBase):
    _identifier = "app_script_condition"

    identifier: str
    name: str
    active: bool
    group: str | None = None
    script: str | None = None
    config: list[dict[str, Any]] | None = Field(default=None)
    app_id: IdField
