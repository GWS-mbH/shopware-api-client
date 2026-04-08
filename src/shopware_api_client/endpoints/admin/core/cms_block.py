from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.cms_block import CmsBlockBase


class CmsBlock(CmsBlockBase, AdminModel["CmsBlockEndpoint"]):
    section: ForeignRelation["CmsSection"] = Field(default=...)
    background_media: ForeignRelation["Media"] = Field(default=...)
    slots: ManyRelation["CmsSlot"] = Field(default=...)


class CmsBlockEndpoint(AdminEndpoint[CmsBlock]):
    name = "cms_block"
    path = "/cms-block"
    model_class = CmsBlock


from .cms_section import CmsSection  # noqa: E402
from .cms_slot import CmsSlot  # noqa: E402
from .media import Media  # noqa: E402
