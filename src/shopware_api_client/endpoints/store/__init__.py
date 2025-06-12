from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...client import StoreClient


from .core.address import Address, AddressEndpoint
from .core.cart import Cart, CartEndpoint
from .core.product import Product, ProductEndpoint

__all__ = ["Address", "Cart", "Product"]


class StoreEndpoints:
    def init_endpoints(self, client: "StoreClient") -> None:
        self.address = AddressEndpoint(client)
        self.cart = CartEndpoint(client)
        self.product = ProductEndpoint(client)

