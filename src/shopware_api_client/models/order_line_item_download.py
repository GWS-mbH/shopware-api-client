from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class OrderLineItemDownloadBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_line_item_download"

    order_line_item_id: IdField
    order_line_item_version_id: IdField | None = None
    media_id: IdField
    position: int
    access_granted: bool
