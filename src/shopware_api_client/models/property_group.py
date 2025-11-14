from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class PropertyGroupBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "property_group"

    name: str
    description: str | None = None
    display_type: str
    sorting_type: str
    filterable: bool | None = None
    visible_on_product_detail_page: bool | None = None
    position: int | None = None
