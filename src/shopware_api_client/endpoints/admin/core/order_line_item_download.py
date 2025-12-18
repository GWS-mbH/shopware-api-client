from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.order_line_item_download import OrderLineItemDownloadBase


class OrderLineItemDownload(OrderLineItemDownloadBase, AdminModel["OrderLineItemDownloadEndpoint"]):
    order_line_item: ForeignRelation["OrderLineItem"] = Field(default=...)
    media: ForeignRelation["Media"] = Field(default=...)


class OrderLineItemDownloadEndpoint(AdminEndpoint[OrderLineItemDownload]):
    name = "order_line_item_download"
    path = "/order-line-item-download"
    model_class = OrderLineItemDownload


from .media import Media  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
