from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class OrderLineItemDownloadBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_line_item_download"

    version_id: IdField | None = None
    order_line_item_id: IdField
    order_line_item_version_id: IdField | None = None
    media_id: IdField
    position: int
    access_granted: bool
    custom_fields: dict[str, Any] | None = None


class OrderLineItemDownloadRelations:
    order_line_item: ForeignRelation["OrderLineItem"]
    media: ForeignRelation["Media"]


class OrderLineItemDownload(OrderLineItemDownloadBase["OrderLineItemDownloadEndpoint"], OrderLineItemDownloadRelations):
    pass


class OrderLineItemDownloadEndpoint(EndpointBase[OrderLineItemDownload]):
    name = "order_line_item_download"
    path = "/order-line-item-download"
    model_class = OrderLineItemDownload


from .media import Media  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
