from typing import Any

from shopware_api_client.base import EndpointMixin, StoreEndpoint
from shopware_api_client.models.customer import Customer as CustomerBase


class Customer(CustomerBase, EndpointMixin["CustomerEndpoint"]):
    group: "CustomerGroup | None" = None
    language: "Language | None" = None
    last_payment_method: "PaymentMethod | None" = None
    default_billing_address: "CustomerAddress | None" = None
    active_billing_address: "CustomerAddress | None" = None
    default_shipping_address: "CustomerAddress | None" = None
    active_shipping_address: "CustomerAddress | None" = None
    salutation: "Salutation | None" = None
    addresses: list["CustomerAddress"] | None = None
    tags: list["Tag"] | None = None


class CustomerEndpoint(StoreEndpoint):
    name = "customer"
    path = "/account/customer"

    async def get(self) -> Customer:
        result: dict[str, Any] = (await self.client.get(self.path)).json()
        return self._parse_response(result, Customer)


from .address import Address as CustomerAddress  # noqa: E402
from .customer_group import CustomerGroup  # noqa: E402
from .language import Language  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .salutation import Salutation  # noqa: E402
from .tag import Tag  # noqa: E402
