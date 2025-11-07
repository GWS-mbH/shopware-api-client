from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.cms_slot import CmsSlot as CmsSlotBase


class CmsSlot(CmsSlotBase, AdminModel["CmsSlotEndpoint"]):
    block: ForeignRelation["CmsBlock"]


class CmsSlotEndpoint(AdminEndpoint[CmsSlot]):
    name = "cms_slot"
    path = "/cms-slot"
    model_class = CmsSlot


from .cms_block import CmsBlock  # noqa: E402
