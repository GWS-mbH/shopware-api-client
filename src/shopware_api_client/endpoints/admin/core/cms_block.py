from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField, Visibility
from ...relations import ForeignRelation, ManyRelation


class CmsBlockBase(ApiModelBase[EndpointClass]):
    _identifier: str = "cms_block"

    position: int
    type: str
    locked: bool | None = None
    name: str | None = None
    section_position: str | None = None
    margin_top: str | None = None
    margin_bottom: str | None = None
    margin_left: str | None = None
    margin_right: str | None = None
    background_color: str | None = None
    background_media_id: IdField | None = None
    background_media_mode: str | None = None
    css_class: str | None = None
    visibility: Visibility | None = None
    section_id: IdField
    custom_fields: dict[str, Any] | None = None
    version_id: IdField | None = None
    cms_section_version_id: IdField | None = None


class CmsBlockRelations:
    section: ForeignRelation["CmsSection"]
    background_media: ForeignRelation["Media"]
    slots: ManyRelation["CmsSlot"]


class CmsBlock(CmsBlockBase["CmsBlockEndpoint"], CmsBlockRelations):
    pass


class CmsBlockEndpoint(EndpointBase[CmsBlock]):
    name = "cms_block"
    path = "/cms-block"
    model_class = CmsBlock


from .cms_section import CmsSection  # noqa: E402
from .cms_slot import CmsSlot  # noqa: E402
from .media import Media  # noqa: E402
