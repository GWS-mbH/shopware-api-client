from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import CompanyTax, CustomerTax
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import CountryState, CurrencyCountryRounding, CustomerAddress, OrderAddress, SalesChannel, TaxRule


class CountryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "country"

    name: str
    iso: str | None = None
    position: int | None = None
    active: bool | None = None
    shipping_available: bool | None = Field(
        default=None,
        serialization_alias="shippingAvailable",
        validation_alias=AliasChoices("shipping_available", "shippingAvailable"),
    )
    iso3: str | None = None
    display_state_in_registration: bool | None = Field(
        default=None,
        serialization_alias="displayStateInRegistration",
        validation_alias=AliasChoices("display_state_in_registration", "displayStateInRegistration"),
    )
    force_state_in_registration: bool | None = Field(
        default=None,
        serialization_alias="forceStateInRegistration",
        validation_alias=AliasChoices("force_state_in_registration", "forceStateInRegistration"),
    )
    check_vat_id_pattern: bool | None = Field(
        default=None,
        serialization_alias="checkVatIdPattern",
        validation_alias=AliasChoices("check_vat_id_pattern", "checkVatIdPattern"),
    )
    vat_id_required: bool | None = Field(
        default=None,
        serialization_alias="vatIdRequired",
        validation_alias=AliasChoices("vat_id_required", "vatIdRequired"),
    )
    vat_id_pattern: str | None = Field(
        default=None,
        serialization_alias="vatIdPattern",
        validation_alias=AliasChoices("vat_id_pattern", "vatIdPattern"),
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    customer_tax: CustomerTax | None = Field(
        default=None, serialization_alias="customerTax", validation_alias=AliasChoices("customer_tax", "customerTax")
    )
    company_tax: CompanyTax | None = Field(
        default=None, serialization_alias="companyTax", validation_alias=AliasChoices("company_tax", "companyTax")
    )
    postal_code_required: bool | None = Field(
        default=None,
        serialization_alias="postalCodeRequired",
        validation_alias=AliasChoices("postal_code_required", "postalCodeRequired"),
    )
    check_postal_code_pattern: bool | None = Field(
        default=None,
        serialization_alias="checkPostalCodePattern",
        validation_alias=AliasChoices("check_postal_code_pattern", "checkPostalCodePattern"),
    )
    check_advanced_postal_code_pattern: bool | None = Field(
        default=None, serialization_alias="checkAdvancedPostalCodePattern"
    )
    advanced_postal_code_pattern: str | None = Field(
        default=None,
        serialization_alias="advancedPostalCodePattern",
        validation_alias=AliasChoices("advanced_postal_code_pattern", "advancedPostalCodePattern"),
    )
    address_format: dict[str, Any] | list[Any] = Field(
        ..., serialization_alias="addressFormat", validation_alias=AliasChoices("address_format", "addressFormat")
    )
    default_postal_code_pattern: str | None = Field(
        default=None,
        serialization_alias="defaultPostalCodePattern",
        validation_alias=AliasChoices("default_postal_code_pattern", "defaultPostalCodePattern"),
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )
    translated: dict[str, Any] | None = None


class CountryRelations:
    states: ClassVar[ManyRelation["CountryState"]] = ManyRelation("CountryState", "states")
    customer_addresses: ClassVar[ManyRelation["CustomerAddress"]] = ManyRelation("CustomerAddress", "customerAddresses")
    order_addresses: ClassVar[ManyRelation["OrderAddress"]] = ManyRelation("OrderAddress", "orderAddresses")
    sales_channel_default_assignments: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "salesChannelDefaultAssignments"
    )
    sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "salesChannels")
    tax_rules: ClassVar[ManyRelation["TaxRule"]] = ManyRelation("TaxRule", "taxRules")
    currency_country_roundings: ClassVar[ManyRelation["CurrencyCountryRounding"]] = ManyRelation(
        "CurrencyCountryRounding", "currencyCountryRoundings"
    )


class Country(CountryBase["CountryEndpoint"], CountryRelations):
    pass


class CountryEndpoint(EndpointBase[Country]):
    name = "country"
    path = "/country"
    model_class = Country


registry.register_admin(CountryEndpoint)
