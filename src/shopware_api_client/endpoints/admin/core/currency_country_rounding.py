from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.currency_country_rounding import CurrencyCountryRoundingBase


class CurrencyCountryRounding(CurrencyCountryRoundingBase, AdminModel["CurrencyCountryRoundingEndpoint"]):
    currency: ForeignRelation["Currency"] = Field(default=...)
    country: ForeignRelation["Country"] = Field(default=...)


class CurrencyCountryRoundingEndpoint(AdminEndpoint[CurrencyCountryRounding]):
    name = "currency_country_rounding"
    path = "/currency-country-rounding"
    model_class = CurrencyCountryRounding


from .country import Country  # noqa: E402
from .currency import Currency  # noqa: E402
