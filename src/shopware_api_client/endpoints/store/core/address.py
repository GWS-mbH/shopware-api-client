from typing import Any, AsyncGenerator

from ....base import EndpointBase
from ....exceptions import SWAPIMethodNotAvailable
from ...admin.core.country import CountryBase
from ...admin.core.country_state import CountryStateBase
from ...admin.core.customer_address import CustomerAddressBase
from ...admin.core.salutation import SalutationBase


class Address(CustomerAddressBase["AddressEndpoint"]):
    _identifier = "address"

    country: CountryBase | None = None
    customer_state: CountryStateBase | None = None
    salutation: SalutationBase | None = None


class AddressEndpoint(EndpointBase[Address]):
    name = "address"
    path = "/account/address"
    model_class = Address
    data_key = "elements"

    async def all(self) -> list[Address] | list[dict[str, Any]]:
        data = self._get_data_dict()

        result = await self.client.post("/account/list-address", json=data)

        result_data: list[dict[str, Any]] = result.json().get(self.data_key, [])

        if self.raw:
            return result_data

        return self._parse_response(result_data)

    async def iter(self, batch_size: int = 100) -> AsyncGenerator[Address | dict[str, Any], None]:
        self._limit = batch_size
        data = self._get_data_dict()
        page = 1

        while True:
            data["page"] = page
            result = await self.client.post("/account/list-address", json=data)

            result_dict: dict[str, Any] = result.json()
            result_data: list[dict[str, Any]] = self._parse_data(result_dict)

            for entry in result_data:
                if self.raw:
                    yield entry
                else:
                    yield self._parse_response(entry)

            if "next" in result_dict.get("links", {}) and len(result_data) > 0:
                page += 1
            else:
                break

    async def set_default_shipping_address(self, pk: str) -> bool:
        result = await self.client.patch(f"/account/address/default-shipping/{pk}")
        return bool(result.status_code == 204)

    async def set_default_billing_address(self, pk: str) -> bool:
        result = await self.client.patch(f"/account/address/default-billing/{pk}")
        return bool(result.status_code == 204)

    async def get(self, pk: str) -> Address | dict[str, Any]:
        raise SWAPIMethodNotAvailable()

    async def bulk_upsert(
        self, objs: list[Address] | list[dict[str, Any]], fail_silently: bool = False, **request_kwargs: Any
    ) -> dict[str, Any]:
        raise SWAPIMethodNotAvailable()

    async def bulk_delete(self, objs: list[Address] | list[dict[str, Any]], fail_silently: bool = False, 
                          **request_kwargs: Any) -> dict[str, Any]:
        raise SWAPIMethodNotAvailable()
