from pydantic import AwareDatetime

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.calculated_price import CalculatedPrice


class QuoteDeliveryBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_delivery"

    quote_id: IdField
    quote_version_id: IdField | None = None
    shipping_method_id: IdField
    shipping_date_earliest: AwareDatetime
    shipping_date_latest: AwareDatetime
    shipping_costs: CalculatedPrice | None = None
