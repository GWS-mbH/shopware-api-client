from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.b2b_components_shopping_list_line_item import B2bComponentsShoppingListLineItemBase


class B2bComponentsShoppingListLineItem(
    B2bComponentsShoppingListLineItemBase, AdminModel["B2bComponentsShoppingListLineItemEndpoint"]
):
    shopping_list: ForeignRelation["B2bComponentsShoppingList"] = Field(default=...)
    product: ForeignRelation["Product"] = Field(default=...)


class B2bComponentsShoppingListLineItemEndpoint(AdminEndpoint[B2bComponentsShoppingListLineItem]):
    name = "b2b_components_shopping_list_line_item"
    path = "/b2b-components-shopping-list-line-item"
    model_class = B2bComponentsShoppingListLineItem


from ..core.product import Product  # noqa: E402
from .b2b_components_shopping_list import B2bComponentsShoppingList  # noqa: E402
