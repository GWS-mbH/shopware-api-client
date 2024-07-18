from typing import Any

from pydantic import AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation


class OrderDeliveryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_delivery"

    version_id: IdField | None = None
    order_id: IdField
    order_version_id: IdField | None = None
    shipping_order_address_id: IdField
    shipping_order_address_version_id: IdField | None = None
    shipping_method_id: IdField
    state_id: IdField = Field(..., exclude=True)
    tracking_codes: list[str]
    shipping_date_earliest: AwareDatetime
    shipping_date_latest: AwareDatetime
    shipping_costs: Amount | None = None
    custom_fields: dict[str, Any] | None = None


class OrderDeliveryRelations:
    state: ForeignRelation["StateMachineState"]
    order: ForeignRelation["Order"]
    shipping_order_address: ForeignRelation["OrderAddress"]
    shipping_method: ForeignRelation["ShippingMethod"]
    positions: ManyRelation["OrderDeliveryPosition"]


class OrderDelivery(OrderDeliveryBase["OrderDeliveryEndpoint"], OrderDeliveryRelations):
    pass


class OrderDeliveryEndpoint(EndpointBase[OrderDelivery]):
    name = "order_delivery"
    path = "/order-delivery"
    model_class = OrderDelivery


from .order import Order  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from .order_delivery_position import OrderDeliveryPosition  # noqa: E402
from .shipping_method import ShippingMethod  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
