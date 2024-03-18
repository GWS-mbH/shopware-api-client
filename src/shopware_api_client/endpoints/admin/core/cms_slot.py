from typing import Any

from pydantic import AliasChoices, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class CmsSlotBase(ApiModelBase[EndpointClass]):
    _identifier: str = "cms_slot"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    type: str
    slot: str
    locked: bool | None = None
    config: dict[str, Any] | None = None
    custom_fields: dict[str, Any] | None = None
    data: dict[str, Any] | None = Field(default=None, exclude=True)
    block_id: IdField
    field_config: dict[str, Any] | None = None
    cms_block_version_id: IdField | None = None
    translated: dict[str, Any] | None = None


class CmsSlotRelations:
    block: ForeignRelation["CmsBlock"]


class CmsSlot(CmsSlotBase["CmsSlotEndpoint"], CmsSlotRelations):
    pass


class CmsSlotEndpoint(EndpointBase[CmsSlot]):
    name = "cms_slot"
    path = "/cms-slot"
    model_class = CmsSlot


from .cms_block import CmsBlock  # noqa: E402
