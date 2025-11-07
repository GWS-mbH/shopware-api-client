from .calculated_price import CalculatedPrice
from .delivery_date import DeliveryDate
from .line_item import LineItem
from ..fieldsets import FieldSetBase


class DeliveryPosition(FieldSetBase):
    delivery_date: DeliveryDate | None = None
    identifier: str | None = None
    line_item: LineItem | None = None
    price: CalculatedPrice | None = None
    quantity: int | None = None
