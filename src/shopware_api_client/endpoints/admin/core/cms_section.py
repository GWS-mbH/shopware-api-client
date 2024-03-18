from typing import Any

from pydantic import AliasChoices, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField, Visibility
from ...relations import ForeignRelation, ManyRelation


class CmsSectionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "cms_section"

    position: int
    type: str
    locked: bool | None = None
    name: str | None = None
    sizing_mode: str | None = Field(
        default=None, serialization_alias="sizingMode", validation_alias=AliasChoices("sizing_mode", "sizingMode")
    )
    mobile_behavior: str | None = None
    background_color: str | None = None
    background_media_id: IdField | None = None
    background_media_mode: str | None = None
    css_class: str | None = None
    page_id: IdField
    visibility: Visibility | None = None
    custom_fields: dict[str, Any] | None = None
    version_id: IdField | None = None
    cms_page_version_id: IdField | None = None


class CmsSectionRelations:
    page: ForeignRelation["CmsPage"]
    background_media: ForeignRelation["Media"]
    blocks: ManyRelation["CmsBlock"]


class CmsSection(CmsSectionBase["CmsSectionEndpoint"], CmsSectionRelations):
    pass


class CmsSectionEndpoint(EndpointBase[CmsSection]):
    name = "cms_section"
    path = "/cms-section"
    model_class = CmsSection


from .cms_block import CmsBlock  # noqa: E402
from .cms_page import CmsPage  # noqa: E402
from .media import Media  # noqa: E402
