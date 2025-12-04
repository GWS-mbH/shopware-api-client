from typing import Literal

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class DeliveryTimeBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "delivery_time"

    name: str
    min: int
    max: int
    unit: Literal["hour", "day", "week", "month", "year"]
