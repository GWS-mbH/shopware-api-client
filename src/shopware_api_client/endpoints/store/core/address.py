from shopware_api_client.base import StoreSearchEndpoint, EndpointMixin
from shopware_api_client.models.customer_address import CustomerAddress as CustomerAddressBase


class Address(CustomerAddressBase, EndpointMixin["AddressEndpoint"]):
    country: "Country | None" = None
    country_state: "CountryState | None" = None
    salutation: "Salutation | None" = None


class AddressEndpoint(StoreSearchEndpoint[Address]):
    model_class = Address
    path = "/account/list-address"

    async def set_default_shipping_address(self, pk: str) -> bool:
        result = await self.client.patch(f"/account/address/default-shipping/{pk}")
        return bool(result.status_code == 204)

    async def set_default_billing_address(self, pk: str) -> bool:
        result = await self.client.patch(f"/account/address/default-billing/{pk}")
        return bool(result.status_code == 204)


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .salutation import Salutation  # noqa: E402
