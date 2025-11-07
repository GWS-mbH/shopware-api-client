from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, Rounding


class CurrencyCountryRounding(ApiModelBase):
    _identifier: str = "currency_country_rounding"

    currency_id: IdField
    country_id: IdField
    item_rounding: Rounding
    total_rounding: Rounding
