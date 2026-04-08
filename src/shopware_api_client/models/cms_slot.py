from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class CmsSlotBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "cms_slot"

    type: str
    slot: str
    locked: bool | None = None
    config: dict[str, Any] | None = Field(default=None)
    data: dict[str, Any] | None = Field(default=None, exclude=True)
    block_id: IdField
    field_config: list[dict[str, Any]] | dict[str, Any] | None = Field(default=None)
    cms_block_version_id: IdField | None = None
