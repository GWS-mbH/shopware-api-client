from .calculated_price import CalculatedPrice
from .delivery_date import DeliveryDate
from .delivery_position import DeliveryPosition
from .shipping_location import ShippingLocation
from ..fieldsets import FieldSetBase


class Delivery(FieldSetBase):
    delivery_date: DeliveryDate | None = None
    location: ShippingLocation | None = None
    positions: list[DeliveryPosition] | None = None
    shipping_costs: CalculatedPrice | None = None
    shipping_method: "ShippingMethod | None" = None


from ..endpoints.store.core.shipping_method import ShippingMethod  # noqa: E402
