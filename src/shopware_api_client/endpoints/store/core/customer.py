from typing import Any

from shopware_api_client.base import EndpointMixin, StoreEndpoint
from shopware_api_client.models.customer import CustomerBase


class Customer(CustomerBase, EndpointMixin["CustomerEndpoint"]):
    group: "CustomerGroup | None" = None
    language: "Language | None" = None
    last_payment_method: "PaymentMethod | None" = None
    default_billing_address: "Address | None" = None
    active_billing_address: "Address | None" = None
    default_shipping_address: "Address | None" = None
    active_shipping_address: "Address | None" = None
    salutation: "Salutation | None" = None
    addresses: list["Address"] | None = None
    tags: list["Tag"] | None = None


class CustomerEndpoint(StoreEndpoint):
    name = "customer"
    path = "/account/customer"

    async def get(self) -> Customer:
        result: dict[str, Any] = (await self.client.get(self.path)).json()
        return self._parse_response(result, Customer)


from .address import Address  # noqa: E402
from .customer_group import CustomerGroup  # noqa: E402
from .language import Language  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .salutation import Salutation  # noqa: E402
from .tag import Tag  # noqa: E402
