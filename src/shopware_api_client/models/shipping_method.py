from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class ShippingMethodBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "shipping_method"

    name: str
    active: bool | None = None
    position: int | None = None
    availability_rule_id: IdField | None = None
    media_id: IdField | None = None
    delivery_time_id: IdField
    tax_type: str
    tax_id: IdField | None = None
    description: str | None = None
    tracking_url: str | None = None
    technical_name: str | None
