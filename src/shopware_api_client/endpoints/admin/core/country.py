from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.country import CountryBase


class Country(CountryBase, AdminModel["CountryEndpoint"]):
    states: ManyRelation["CountryState"] = Field(default=...)
    customer_addresses: ManyRelation["CustomerAddress"] = Field(default=...)
    order_addresses: ManyRelation["OrderAddress"] = Field(default=...)
    sales_channel_default_assignments: ManyRelation["SalesChannel"] = Field(default=...)
    sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    tax_rules: ManyRelation["TaxRule"] = Field(default=...)
    currency_country_roundings: ManyRelation["CurrencyCountryRounding"] = Field(default=...)


class CountryEndpoint(AdminEndpoint[Country]):
    name = "country"
    path = "/country"
    model_class = Country


from .country_state import CountryState  # noqa: E402
from .currency_country_rounding import CurrencyCountryRounding  # noqa: E402
from .customer_address import CustomerAddress  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .tax_rule import TaxRule  # noqa: E402
