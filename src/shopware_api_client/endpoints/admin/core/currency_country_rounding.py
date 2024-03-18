from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField, Rounding
from ...relations import ForeignRelation


class CurrencyCountryRoundingBase(ApiModelBase[EndpointClass]):
    _identifier: str = "currency_country_rounding"

    currency_id: IdField
    country_id: IdField
    item_rounding: Rounding
    total_rounding: Rounding


class CurrencyCountryRoundingRelations:
    currency: ForeignRelation["Currency"]
    country: ForeignRelation["Country"]


class CurrencyCountryRounding(
    CurrencyCountryRoundingBase["CurrencyCountryRoundingEndpoint"], CurrencyCountryRoundingRelations
):
    pass


class CurrencyCountryRoundingEndpoint(EndpointBase[CurrencyCountryRounding]):
    name = "currency_country_rounding"
    path = "/currency-country-rounding"
    model_class = CurrencyCountryRounding


from .country import Country  # noqa: E402
from .currency import Currency  # noqa: E402
