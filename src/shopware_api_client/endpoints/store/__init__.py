from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from shopware_api_client.client import StoreClient
    from shopware_api_client.endpoints.base_fields import IdField

from .core.address import Address, AddressEndpoint
from .core.cart import Cart, CartEndpoint
from .core.context import Context, ContextEndpoint
from .core.country import Country, CountryEndpoint
from .core.country_state import CountryState, CountryStateEndpoint
from .core.currency import Currency, CurrencyEndpoint
from .core.customer import Customer, CustomerEndpoint
from .core.language import Language, LanguageEndpoint
from .core.order import Order, OrderEndpoint
from .core.product import Product, ProductEndpoint
from .core.salutation import Salutation, SalutationEndpoint

__all__ = [
    "Address",
    "Cart",
    "Context",
    "Country",
    "CountryState",
    "Currency",
    "Customer",
    "Language",
    "Order",
    "Product",
    "Salutation",
    "StoreEndpoints",
]


class StoreEndpoints:
    def init_endpoints(self, client: "StoreClient") -> None:
        self.address = AddressEndpoint(client)
        self.cart = CartEndpoint(client)
        self.country = CountryEndpoint(client)
        self.context = ContextEndpoint(client)
        self.country_state: Callable[["IdField"], CountryStateEndpoint] = lambda country_id: CountryStateEndpoint(
            client=client, country_id=country_id
        )
        self.currency = CurrencyEndpoint(client)
        self.customer = CustomerEndpoint(client)
        self.language = LanguageEndpoint(client)
        self.order = OrderEndpoint(client)
        self.product = ProductEndpoint(client)
        self.salutation = SalutationEndpoint(client)
