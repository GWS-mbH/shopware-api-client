from .delivery_time import DeliveryTime
from ..fieldsets import FieldSetBase


class DeliveryInformation(FieldSetBase):
    free_delivery: bool | None = None
    delivery_time: DeliveryTime | None = None
    height: float | None = None
    length: float | None = None
    restock_time: int | None = None
    stock: int | None = None
    weight: float | None = None
    width: float | None = None
