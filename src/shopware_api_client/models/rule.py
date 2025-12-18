from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class RuleBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "rule"

    name: str
    priority: int
    description: str | None = None
    invalid: bool | None = Field(default=None, exclude=True)
    areas: list[str] | None = Field(default=None, exclude=True)
    module_types: list[str] | dict[str, Any] | None = Field(default=None)
