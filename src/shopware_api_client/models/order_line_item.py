from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.structs.absolute_price_definition import AbsolutePriceDefinition
from shopware_api_client.structs.quantity_price_definition import QuantityPriceDefinition
from shopware_api_client.structs.reference_price_definition import ReferencePriceDefinition


class OrderLineItemBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_line_item"

    order_id: IdField
    order_version_id: IdField | None = None
    product_id: IdField | None = None
    product_version_id: IdField | None = None
    promotion_id: IdField | None = Field(default=None, exclude=True)
    parent_id: IdField | None = None
    parent_version_id: IdField | None = None
    cover_id: IdField | None = None
    identifier: str
    referenced_id: str | None = None
    quantity: int
    label: str
    payload: dict[str, Any] | list | None = Field(default=None)
    good: bool | None = None
    removable: bool | None = None
    stackable: bool | None = None
    position: int
    states: list[str]
    price_definition: AbsolutePriceDefinition | QuantityPriceDefinition | ReferencePriceDefinition | None = None
    unit_price: float | None = None
    total_price: float | None = None
    description: str | None = None
    type: str | None = None
