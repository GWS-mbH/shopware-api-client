from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, Price


class B2bComponentsShoppingListBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "b2b_components_shopping_list"

    name: str | None = None
    active: bool | None = None
    price: Price | None = None
    sales_channel_id: IdField | None = None
    customer_id: IdField | None = None
    employee_id: IdField | None = None
