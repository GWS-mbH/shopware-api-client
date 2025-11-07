from shopware_api_client.fieldsets import FieldSetBase


class ShippingLocation(FieldSetBase):
    country: "Country | None" = None
    address: "Address | None" = None
    state: "CountryState | None" = None


from ..endpoints.store.core.address import Address  # noqa: E402
from ..endpoints.store.core.country import Country  # noqa: E402
from ..endpoints.store.core.country_state import CountryState  # noqa: E402
