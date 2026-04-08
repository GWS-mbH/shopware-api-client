from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.cms_section import CmsSectionBase


class CmsSection(CmsSectionBase, AdminModel["CmsSectionEndpoint"]):
    page: ForeignRelation["CmsPage"] = Field(default=...)
    background_media: ForeignRelation["Media"] = Field(default=...)
    blocks: ManyRelation["CmsBlock"] = Field(default=...)


class CmsSectionEndpoint(AdminEndpoint[CmsSection]):
    name = "cms_section"
    path = "/cms-section"
    model_class = CmsSection


from .cms_block import CmsBlock  # noqa: E402
from .cms_page import CmsPage  # noqa: E402
from .media import Media  # noqa: E402
