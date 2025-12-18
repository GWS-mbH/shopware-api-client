from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.cash_rounding_config import CashRoundingConfig


class CurrencyCountryRoundingBase(ApiModelBase):
    _identifier: str = "currency_country_rounding"

    currency_id: IdField
    country_id: IdField
    item_rounding: CashRoundingConfig
    total_rounding: CashRoundingConfig
