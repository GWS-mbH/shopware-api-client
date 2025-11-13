from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.country import CountryBase


class Country(CountryBase, AdminModel["CountryEndpoint"]):
    states: ManyRelation["CountryState"]
    customer_addresses: ManyRelation["CustomerAddress"]
    order_addresses: ManyRelation["OrderAddress"]
    sales_channel_default_assignments: ManyRelation["SalesChannel"]
    sales_channels: ManyRelation["SalesChannel"]
    tax_rules: ManyRelation["TaxRule"]
    currency_country_roundings: ManyRelation["CurrencyCountryRounding"]


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
