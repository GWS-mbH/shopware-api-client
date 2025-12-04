from typing import Any

from shopware_api_client.base import StoreSearchEndpoint, EndpointMixin, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.fieldsets import FieldSetBase
from shopware_api_client.models.customer_address import CustomerAddressBase


class Address(CustomerAddressBase, EndpointMixin["AddressEndpoint"]):
    country: "Country | None" = None
    country_state: "CountryState | None" = None
    salutation: "Salutation | None" = None


class AddressUpdateSchema(FieldSetBase, CustomFieldsMixin):
    country_id: IdField
    country_state_id: IdField | None = None
    salutation_id: IdField | None = None
    first_name: str
    last_name: str
    zipcode: str | None = None
    city: str
    company: str | None = None
    street: str
    department: str | None = None
    title: str | None = None
    phone_number: str | None = None
    additional_address_line1: str | None = None
    additional_address_line2: str | None = None


class AddressEndpoint(StoreSearchEndpoint[Address]):
    model_class = Address
    path = "/account/list-address"

    async def delete(self, pk: IdField) -> bool:
        result = await self.client.delete(f"/account/address/{pk}")
        return bool(result.is_success)

    async def modify(self, pk: IdField, obj: AddressUpdateSchema) -> Address:
        data = obj.model_dump_json(by_alias=True)
        result: dict[str, Any] = (await self.client.patch(f"/account/address/{pk}", data=data)).json()
        return self._parse_response(result, Address)

    async def create(self, obj: AddressUpdateSchema) -> Address:
        data = obj.model_dump_json(by_alias=True)
        result: dict[str, Any] = (await self.client.post("/account/address", data=data)).json()
        return self._parse_response(result, Address)

    async def set_default_shipping_address(self, pk: IdField) -> bool:
        result = await self.client.patch(f"/account/address/default-shipping/{pk}")
        return bool(result.is_success)

    async def set_default_billing_address(self, pk: IdField) -> bool:
        result = await self.client.patch(f"/account/address/default-billing/{pk}")
        return bool(result.is_success)


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .salutation import Salutation  # noqa: E402
