from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import CompanyTax, CustomerTax
from ...relations import ManyRelation


class CountryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "country"

    name: str
    iso: str | None = None
    position: int | None = None
    active: bool | None = None
    shipping_available: bool | None = None
    iso3: str | None = None
    display_state_in_registration: bool | None = None
    force_state_in_registration: bool | None = None
    check_vat_id_pattern: bool | None = None
    vat_id_required: bool | None = None
    vat_id_pattern: str | None = None
    custom_fields: dict[str, Any] | None = None
    customer_tax: CustomerTax | None = None
    company_tax: CompanyTax | None = None
    postal_code_required: bool | None = None
    check_postal_code_pattern: bool | None = None
    check_advanced_postal_code_pattern: bool | None = None
    advanced_postal_code_pattern: str | None = None
    address_format: dict[str, Any] | list[Any]
    default_postal_code_pattern: str | None = None
    translated: dict[str, Any] | None = None


class CountryRelations:
    states: ManyRelation["CountryState"]
    customer_addresses: ManyRelation["CustomerAddress"]
    order_addresses: ManyRelation["OrderAddress"]
    sales_channel_default_assignments: ManyRelation["SalesChannel"]
    sales_channels: ManyRelation["SalesChannel"]
    tax_rules: ManyRelation["TaxRule"]
    currency_country_roundings: ManyRelation["CurrencyCountryRounding"]


class Country(CountryBase["CountryEndpoint"], CountryRelations):
    pass


class CountryEndpoint(EndpointBase[Country]):
    name = "country"
    path = "/country"
    model_class = Country


from .country_state import CountryState  # noqa: E402
from .currency_country_rounding import CurrencyCountryRounding  # noqa: E402
from .customer_address import CustomerAddress  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .tax_rule import TaxRule  # noqa: E402
