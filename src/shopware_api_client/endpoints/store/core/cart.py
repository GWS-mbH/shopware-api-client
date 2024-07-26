from typing import Any

from shopware_api_client.base import ApiModelBase, EndpointBase, EndpointClass
from shopware_api_client.endpoints.base_fields import IdField, Price


class ItemPrice(ApiModelBase[EndpointClass]):
    unit_price: float
    quantity: int
    total_price: float
    calculated_taxes: list[dict[str, Any]] | None = None
    tax_rules: list[dict[str, Any]] | None = None
    reference_price: float | None = None
    list_price: float | None = None
    regulation_price: float | None = None


class LineItem(ApiModelBase[EndpointClass]):
    _identifier: str = "cart_line_item"
    
    payload: dict[str, Any]
    label: str
    quantity: int
    price_definition: dict[str, Any]
    price: ItemPrice
    good: bool
    description: str | None = None
    cover: Any
    delivery_information: dict[str, Any]
    children: list[Any]
    removable: bool
    stackable: bool
    quantity_information: dict[str, Any]
    modified: bool
    data_timestamp: str
    data_context_hash: str
    states: list[str]
    modified_by_app: bool
    referenced_id: IdField


class Position(ApiModelBase[EndpointClass]):
    _identifier: str = "cart_delivery_position"
    
    delivery_date: str
    line_items: list[LineItem]
    price: ItemPrice


class CartDelivery(ApiModelBase[EndpointClass]):
    _identifier: str = "cart_delivery"
    
    delilvery_date: str
    location: str
    positions:list[dict[str, Any]]
    shipping_costs: str
    shipping_method: str


class Cart(ApiModelBase["CartEndpoint"]):
    _identifier: str = "cart"
    
    token: str
    price: Price
    line_items: list[LineItem]
    errors: list[dict[str, Any]]
    deliveries: list[dict[str, CartDelivery]]
    transactions: list[dict[str, Any]]
    modified: bool
    customer_comment: str | None = None
    affiliate_code: str | None = None
    campaign_code: str | None = None


class CartEndpoint(EndpointBase[Cart]):
    name = "cart"
    path = "/checkout/cart"
    model_class = Cart
    data_key = "elements"


    async def first(self) -> Cart:
        result = await self.client.get(self.path)
        result_data: dict[str, Any] = result.json()
        return self._parse_response(result_data)
