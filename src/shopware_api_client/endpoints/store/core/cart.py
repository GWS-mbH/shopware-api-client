from typing import Any

from shopware_api_client.base import StoreEndpoint, EndpointMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.cart import Cart as CartBase
from shopware_api_client.structs.line_item import LineItem


class Cart(CartBase, EndpointMixin["CartEndpoint"]):
    pass


class CartEndpoint(StoreEndpoint):
    name = "cart"
    path = "/checkout/cart"

    # kept for backwards-compatibility
    async def first(self) -> Cart:
        return await self.fetch_or_create()

    async def fetch_or_create(self) -> Cart:
        result: dict[str, Any] = (await self.client.get(self.path)).json()
        return self._parse_response(result, cls=Cart)

    async def delete(self) -> bool:
        response = await self.client.delete(self.path)
        return bool(response.is_success)

    async def add_items(self, items: list["LineItem"]) -> Cart:
        result: dict[str, Any] = (
            await self.client.post(
                f"{self.path}/line-item",
                json={"items": [item.model_dump(by_alias=True, mode="json", exclude_unset=True) for item in items]},
            )
        ).json()
        return self._parse_response(result, cls=Cart)

    async def update_items(self, items: list["LineItem"]) -> Cart:
        result: dict[str, Any] = (
            await self.client.patch(
                f"{self.path}/line-item",
                json={"items": [item.model_dump(by_alias=True, mode="json", exclude_unset=True) for item in items]},
            )
        ).json()
        return self._parse_response(result, cls=Cart)

    async def remove_items(self, ids: list[IdField]) -> Cart:
        result: dict[str, Any] = (await self.client.post(f"{self.path}/line-item/delete", json={"ids": ids})).json()
        return self._parse_response(result, cls=Cart)
