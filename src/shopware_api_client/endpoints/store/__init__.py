from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...client import StoreClient


from .core.address import Address, AddressEndpoint

__all__ = ["Address"]


class StoreEndpoints:
    def init_endpoints(self, client: "StoreClient") -> None:
        self.address = AddressEndpoint(client)
