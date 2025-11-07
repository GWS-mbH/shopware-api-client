from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.cms_section import CmsSection as CmsSectionBase


class CmsSection(CmsSectionBase, AdminModel["CmsSectionEndpoint"]):
    page: ForeignRelation["CmsPage"]
    background_media: ForeignRelation["Media"]
    blocks: ManyRelation["CmsBlock"]


class CmsSectionEndpoint(AdminEndpoint[CmsSection]):
    name = "cms_section"
    path = "/cms-section"
    model_class = CmsSection


from .cms_block import CmsBlock  # noqa: E402
from .cms_page import CmsPage  # noqa: E402
from .media import Media  # noqa: E402
