from typing import Any

from shopware_api_client.base import StoreEndpoint, EndpointMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.sales_channel_context import SalesChannelContext


class Context(SalesChannelContext, EndpointMixin["ContextEndpoint"]):
    pass


class ContextEndpoint(StoreEndpoint):
    name = "context"
    path = "/context"

    async def get(self) -> Context:
        result: dict[str, Any] = (await self.client.get(self.path)).json()
        return self._parse_response(result, Context)

    async def modifiy(
        self,
        currency_id: IdField | None = None,
        language_id: IdField | None = None,
        billing_address_id: IdField | None = None,
        shipping_address_id: IdField | None = None,
        payment_method_id: IdField | None = None,
        shipping_method_id: IdField | None = None,
        country_id: IdField | None = None,
        country_state_id: IdField | None = None,
    ) -> bool:
        data: dict[str, Any] = {}

        if currency_id is not None:
            data["currencyId"] = currency_id

        if language_id is not None:
            data["languageId"] = language_id

        if billing_address_id is not None:
            data["billingAddressId"] = billing_address_id

        if shipping_address_id is not None:
            data["shippingAddressId"] = shipping_address_id

        if payment_method_id is not None:
            data["paymentMethodId"] = payment_method_id

        if shipping_method_id is not None:
            data["shippingMethodId"] = shipping_method_id

        if country_id is not None:
            data["countryId"] = country_id

        if country_state_id is not None:
            data["countryStateId"] = country_state_id

        response = await self.client.patch(self.path, json=data)
        return bool(response.is_success)
