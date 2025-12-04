from shopware_api_client.models.order_address import OrderAddressBase


class OrderAddress(OrderAddressBase):
    country: "Country | None" = None
    country_state: "CountryState | None" = None
    salutation: "Salutation | None" = None


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .salutation import Salutation  # noqa: E402
