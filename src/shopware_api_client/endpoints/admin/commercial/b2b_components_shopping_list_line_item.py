from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField, Price
from ...relations import ForeignRelation


class B2bComponentsShoppingListLineItemBase(ApiModelBase[EndpointClass]):
    _identifier: str = "b2b_components_shopping_list_line_item"
    product_id: IdField
    product_version_id: IdField | None = None
    quantity: int
    price: Price | None = None
    custom_fields: dict[str, Any] | None = None
    shopping_list_id: IdField


class B2bComponentsShoppingListLineItemRelations:
    shopping_list: ForeignRelation["B2bComponentsShoppingList"]
    product: ForeignRelation["Product"]


class B2bComponentsShoppingListLineItem(
    B2bComponentsShoppingListLineItemBase["B2bComponentsShoppingListLineItemEndpoint"],
    B2bComponentsShoppingListLineItemRelations,
):
    pass


class B2bComponentsShoppingListLineItemEndpoint(EndpointBase[B2bComponentsShoppingListLineItem]):
    name = "b2b_components_shopping_list_line_item"
    path = "/b2b-components-shopping-list-line-item"
    model_class = B2bComponentsShoppingListLineItem


from ..core.product import Product  # noqa: E402
from .b2b_components_shopping_list import B2bComponentsShoppingList  # noqa: E402
