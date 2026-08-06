from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.absolute_price_definition import AbsolutePriceDefinition
from shopware_api_client.structs.calculated_price import CalculatedPrice
from shopware_api_client.structs.price import Price
from shopware_api_client.structs.quantity_price_definition import QuantityPriceDefinition
from shopware_api_client.structs.reference_price_definition import ReferencePriceDefinition


class QuoteLineItemBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "quote_line_item"

    quote_id: IdField
    quote_version_id: IdField | None = None
    identifier: str
    parent_id: IdField | None = None
    parent_version_id: IdField | None = None
    product_id: IdField | None = None
    product_version_id: IdField | None = None
    promotion_id: IdField | None = Field(default=None, exclude=True)
    states: list[str]
    label: str
    description: str | None = None
    quantity: int
    type: str | None = None
    payload: dict[str, Any] | list | None = Field(default=None)
    unit_price: float | None = None
    total_price: float | None = None
    price_definition: AbsolutePriceDefinition | QuantityPriceDefinition | ReferencePriceDefinition | None = None
    price: CalculatedPrice | None = None
    product_price: list[Price] | None = None
    purchase_price: list[Price] | None = None
    discount: dict[str, Any] | None = Field(default=None)
    good: bool | None = None
    removable: bool | None = None
    stackable: bool | None = None
    position: int
    referenced_id: str | None = None
    cover_id: IdField | None = None
