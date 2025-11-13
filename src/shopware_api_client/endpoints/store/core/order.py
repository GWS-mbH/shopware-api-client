from typing import Any

from shopware_api_client.base import StoreSearchEndpoint, EndpointMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.models.order import OrderBase


class Order(OrderBase, EndpointMixin["OrderEndpoint"]):
    state_machine_state: "StateMachineState"
    primary_order_delivery: "OrderDelivery | None" = None
    primary_order_transaction: "OrderTransaction | None" = None
    order_customer: "OrderCustomer | None" = None
    currency: "Currency | None" = None
    language: "Language | None" = None
    addresses: list["OrderAddress"] | None = None
    billing_address: "OrderAddress | None" = None
    deliveries: list["OrderDelivery"] | None = None
    line_items: list["OrderLineItem"] | None = None
    transactions: list["OrderTransaction"] | None = None
    documents: list["Document"] | None = None
    tags: list["Tag"] | None = None


class OrderEndpoint(StoreSearchEndpoint[Order]):
    model_class = Order
    path = "/order"

    async def create_from_cart(
        self, customer_comment: str | None = None, affiliate_code: str | None = None, campaign_code: str | None = None
    ) -> Order:
        data: dict[str, str] = {}

        if customer_comment is not None:
            data["customerComment"] = customer_comment

        if affiliate_code is not None:
            data["affiliateCode"] = affiliate_code

        if campaign_code is not None:
            data["campaignCode"] = campaign_code

        response = await self.client.post("/checkout/order", json=data)
        result: dict[str, Any] = response.json()

        return self._parse_response(result, cls=Order)

    async def cancel(self, order_id: IdField) -> "StateMachineState":
        result: dict[str, Any] = (await self.client.post("/order/state/cancel", json={"orderId": order_id})).json()
        return self._parse_response(result, StateMachineState)

    async def update_payment_method(self, payment_method_id: IdField, order_id: IdField) -> bool:
        result = await self.client.post(
            "/order/payment", json={"paymentMethodId": payment_method_id, "orderId": order_id}
        )
        return bool(result.is_success)


from .currency import Currency  # noqa: E402
from .document import Document  # noqa: E402
from .language import Language  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from .order_customer import OrderCustomer  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .order_line_item import OrderLineItem  # noqa: E402
from .order_transaction import OrderTransaction  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
from .tag import Tag  # noqa: E402
