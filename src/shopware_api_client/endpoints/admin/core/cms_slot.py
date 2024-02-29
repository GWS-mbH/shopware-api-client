from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import CmsBlock


class CmsSlotBase(ApiModelBase[EndpointClass]):
    _identifier: str = "cms_slot"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    type: str
    slot: str
    locked: bool | None = None
    config: dict[str, Any] | None = None
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    data: dict[str, Any] | None = Field(default=None, exclude=True)
    block_id: IdField = Field(..., serialization_alias="blockId", validation_alias=AliasChoices("block_id", "blockId"))
    field_config: dict[str, Any] | None = Field(
        default=None, serialization_alias="fieldConfig", validation_alias=AliasChoices("field_config", "fieldConfig")
    )
    cms_block_version_id: IdField | None = Field(
        default=None,
        serialization_alias="cmsBlockVersionId",
        validation_alias=AliasChoices("cms_block_version_id", "cmsBlockVersionId"),
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


class CmsSlotRelations:
    block: ClassVar[ForeignRelation["CmsBlock"]] = ForeignRelation("CmsBlock", "block_id")


class CmsSlot(CmsSlotBase["CmsSlotEndpoint"], CmsSlotRelations):
    pass


class CmsSlotEndpoint(EndpointBase[CmsSlot]):
    name = "cms_slot"
    path = "/cms-slot"
    model_class = CmsSlot


registry.register_admin(CmsSlotEndpoint)
