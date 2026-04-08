from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.structs.tax_free_config import TaxFreeConfig


class CountryBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "country"

    name: str
    iso: str | None = None
    position: int | None = None
    active: bool | None = None
    shipping_available: bool | None = None
    iso3: str | None = None
    display_state_in_registration: bool | None = None
    force_state_in_registration: bool | None = None
    check_vat_id_pattern: bool | None = None
    var_id_pattern: str | None = None
    vat_id_required: bool | None = None
    customer_tax: TaxFreeConfig | None = None
    company_tax: TaxFreeConfig | None = None
    postal_code_required: bool | None = None
    is_eu: bool | None = None
    check_postal_code_pattern: bool | None = None
    check_advanced_postal_code_pattern: bool | None = None
    advanced_postal_code_pattern: str | None = None
    default_postal_code_pattern: str | None = None
    address_format: list[list[str]]
