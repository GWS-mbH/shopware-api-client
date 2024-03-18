from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class PropertyGroupBase(ApiModelBase[EndpointClass]):
    _identifier: str = "property_group"

    name: str
    description: str | None = None
    display_type: str
    sorting_type: str
    filterable: bool | None = None
    visible_on_product_detail_page: bool | None = None
    position: int | None = None
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class PropertyGroupRelations:
    options: ManyRelation["PropertyGroupOption"]


class PropertyGroup(PropertyGroupBase["PropertyGroupEndpoint"], PropertyGroupRelations):
    pass


class PropertyGroupEndpoint(EndpointBase[PropertyGroup]):
    name = "property_group"
    path = "/property-group"
    model_class = PropertyGroup


from .property_group_option import PropertyGroupOption  # noqa: E402
