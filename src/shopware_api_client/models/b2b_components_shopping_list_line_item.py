from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, Price


class B2bComponentsShoppingListLineItem(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "b2b_components_shopping_list_line_item"

    product_id: IdField
    product_version_id: IdField | None = None
    quantity: int
    price: Price | None = None
    shopping_list_id: IdField
