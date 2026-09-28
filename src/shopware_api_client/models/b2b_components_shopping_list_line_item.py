from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.calculated_price import CalculatedPrice


class B2bComponentsShoppingListLineItemBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "b2b_components_shopping_list_line_item"

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    quantity: int
    price: CalculatedPrice | None = None
    shopping_list_id: Annotated[IdField, RefersTo("b2b_components_shopping_list")]
