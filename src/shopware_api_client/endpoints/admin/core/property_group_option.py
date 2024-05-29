from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class PropertyGroupOptionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "property_group_option"

    group_id: IdField | None = None
    name: str | None = None
    position: int | None = None
    color_hex_code: str | None = None
    media_id: IdField | None = None
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class PropertyGroupOptionRelations:
    media: ForeignRelation["Media"]
    group: ForeignRelation["PropertyGroup"]
    product_configurator_settings: ManyRelation["ProductConfiguratorSetting"]
    product_properties: ManyRelation["Product"]
    product_options: ManyRelation["Product"]


class PropertyGroupOption(PropertyGroupOptionBase["PropertyGroupOptionEndpoint"], PropertyGroupOptionRelations):
    pass


class PropertyGroupOptionEndpoint(EndpointBase[PropertyGroupOption]):
    name = "property_group_option"
    path = "/property-group-option"
    model_class = PropertyGroupOption


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .product_configurator_setting import ProductConfiguratorSetting  # noqa: E402
from .property_group import PropertyGroup  # noqa: E402
