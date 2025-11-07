

from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Price
from ...relations import ForeignRelation, ManyRelation


class B2bComponentsShoppingListBase(ApiModelBase[EndpointClass]):
    _identifier: str = "b2b_components_shopping_list"

    name: str | None = None
    active: bool | None = None
    custom_fields: dict[str, Any] | None = None
    price: Price | None = None
    sales_channel_id: str | None = None
    customer_id: str | None = None
    employee_id: str | None = None


class B2bComponentsShoppingListRelations:
    sales_channel: ForeignRelation["SalesChannel"]
    line_items: ManyRelation["B2bComponentsShoppingListLineItem"]
    customer: ForeignRelation["Customer"]
    employee: ForeignRelation["B2bEmployee"]


class B2bComponentsShoppingList(B2bComponentsShoppingListBase["B2bComponentsShoppingListEndpoint"], B2bComponentsShoppingListRelations):
    pass


class B2bComponentsShoppingListEndpoint(EndpointBase[B2bComponentsShoppingList]):
    name = "b2b_components_shopping_list"
    path = "/b2b-components-shopping-list"
    model_class = B2bComponentsShoppingList


from ..core.customer import Customer  # noqa: E402
from ..core.sales_channel import SalesChannel  # noqa: E402
from .b2b_components_shopping_list_line_item import B2bComponentsShoppingListLineItem  # noqa: E402
from .b2b_employee import B2bEmployee  # noqa: E402
