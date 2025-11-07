from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.currency_country_rounding import CurrencyCountryRounding as CurrencyCountryRoundingBase


class CurrencyCountryRounding(CurrencyCountryRoundingBase, AdminModel["CurrencyCountryRoundingEndpoint"]):
    currency: ForeignRelation["Currency"]
    country: ForeignRelation["Country"]


class CurrencyCountryRoundingEndpoint(AdminEndpoint[CurrencyCountryRounding]):
    name = "currency_country_rounding"
    path = "/currency-country-rounding"
    model_class = CurrencyCountryRounding


from .country import Country  # noqa: E402
from .currency import Currency  # noqa: E402
