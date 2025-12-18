from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.b2b_components_shopping_list import B2bComponentsShoppingListBase


class B2bComponentsShoppingList(B2bComponentsShoppingListBase, AdminModel["B2bComponentsShoppingListEndpoint"]):
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    line_items: ManyRelation["B2bComponentsShoppingListLineItem"] = Field(default=...)
    customer: ForeignRelation["Customer"] = Field(default=...)
    employee: ForeignRelation["B2bEmployee"] = Field(default=...)


class B2bComponentsShoppingListEndpoint(AdminEndpoint[B2bComponentsShoppingList]):
    name = "b2b_components_shopping_list"
    path = "/b2b-components-shopping-list"
    model_class = B2bComponentsShoppingList


from ..core.customer import Customer  # noqa: E402
from ..core.sales_channel import SalesChannel  # noqa: E402
from .b2b_components_shopping_list_line_item import B2bComponentsShoppingListLineItem  # noqa: E402
from .b2b_employee import B2bEmployee  # noqa: E402
