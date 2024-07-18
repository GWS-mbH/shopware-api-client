from typing import Any

from shopware_api_client.base import ApiModelBase, EndpointBase


class LineItem(ApiModelBase["CartEndpoint"]):
    _identifier: str = "cart_line_item"
    
    payload: dict[str, Any]
    label: str
    quantity: int
    priceDefinition: dict[str, Any]
    price: dict[str, Any]
    good: bool
    description: str
    cover: Any
    deliveryInformation: dict[str, Any]
    chidlren: list[Any]
    # requirement: ?
    removable: bool
    stackable: bool
    quantityInformation: dict[str, Any]
    modified: bool
    dataTimestamp: str
    dataContextHash: str
    uniqueIdentifier: str = "cart_line_item"
    states: list[str]
    modifiedByApp: bool
    id: str
    type: str
    referencedId: str
    apiAlias: str


class Cart(ApiModelBase["CartEndpoint"]):
    _identifier: str = "cart"
    
    token: str
    price: dict[str, Any]
    lineItems: list[dict[str, Any]]
    errors: list[dict[str, Any]]
    deliveries: list[dict[str, Any]]
    transactions: list[dict[str, Any]]
    modified: bool
    customerComment: str | None = None
    affiliateCode: str | None = None
    campaignCode: str | None = None


class CartEndpoint(EndpointBase[Cart]):
    name = "cart"
    path = "/checkout/cart"
    model_class = Cart
    data_key = "elements"


    async def first(self) -> Cart:
        result = await self.client.get(self.path)
        result_data: dict[str, Any] = result.json()
        return self._parse_response(result_data)
