from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ShippingMethodBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "shipping_method"

    name: str
    active: bool | None = None
    position: int | None = None
    availability_rule_id: Annotated[IdField | None, RefersTo("rule")] = None
    media_id: Annotated[IdField | None, RefersTo("media")] = None
    delivery_time_id: Annotated[IdField, RefersTo("delivery_time")]
    tax_type: str
    tax_id: Annotated[IdField | None, RefersTo("tax")] = None
    description: str | None = None
    tracking_url: str | None = None
    technical_name: str | None
