from typing import Any

from shopware_api_client.base import ApiModelBase, EndpointBase
from shopware_api_client.endpoints.admin.core.country import Country
from shopware_api_client.endpoints.base_fields import BaseFieldSet, IdField, Price
from shopware_api_client.endpoints.store.core.address import Address


class ItemPrice(BaseFieldSet):
    unit_price: float
    quantity: int
    total_price: float
    calculated_taxes: list[dict[str, Any]] | None = None
    tax_rules: list[dict[str, Any]] | None = None
    reference_price: float | None = None
    list_price: float | None = None
    regulation_price: float | None = None
    

class ShippingCosts(ItemPrice):
    raw_total: float | None = None
    position_price: float | None = None
    net_price: float | None = None
    has_range: bool | None = None
    variant: str | None = None


class LineItem(BaseFieldSet):
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


class DeliveryPosition(BaseFieldSet):
    delivery_date: Any
    line_item: LineItem
    price: ItemPrice


class Location(BaseFieldSet):
    country: Country
    adress: Address | None = None
    state: Any | None = None
    

class CartDelivery(BaseFieldSet):
    delilvery_date: Any | None = None
    location: Location | None = None
    positions: list[DeliveryPosition] | None = None
    shipping_costs: ShippingCosts | None = None #ShippingCosts 
    shipping_method: Any | None = None


class Cart(ApiModelBase["CartEndpoint"]):
    _identifier: str = "cart"
    
    token: str
    price: Price
    line_items: list[LineItem]
    errors: list[dict[str, Any]] | dict[str, Any] | None = None
    deliveries: list[CartDelivery]
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
