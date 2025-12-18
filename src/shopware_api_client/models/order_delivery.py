from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.calculated_price import CalculatedPrice


class OrderDeliveryBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_delivery"

    order_id: IdField
    order_version_id: IdField | None = None
    shipping_order_address_id: IdField
    shipping_order_address_version_id: IdField | None = None
    shipping_method_id: IdField
    state_id: IdField = Field(..., exclude=True)
    tracking_codes: list[str]
    shipping_date_earliest: AwareDatetime
    shipping_date_latest: AwareDatetime
    shipping_costs: CalculatedPrice | None = None
