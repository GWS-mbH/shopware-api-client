from shopware_api_client.models.cms_slot import CmsSlotBase


class CmsSlot(CmsSlotBase):
    block: "CmsBlock | None" = None


from .cms_block import CmsBlock  # noqa: E402
