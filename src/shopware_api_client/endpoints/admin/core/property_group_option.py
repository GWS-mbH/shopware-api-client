from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.property_group_option import PropertyGroupOptionBase


class PropertyGroupOption(PropertyGroupOptionBase, AdminModel["PropertyGroupOptionEndpoint"]):
    media: ForeignRelation["Media"]
    group: ForeignRelation["PropertyGroup"]
    product_configurator_settings: ManyRelation["ProductConfiguratorSetting"]
    product_properties: ManyRelation["Product"]
    product_options: ManyRelation["Product"]


class PropertyGroupOptionEndpoint(AdminEndpoint[PropertyGroupOption]):
    name = "property_group_option"
    path = "/property-group-option"
    model_class = PropertyGroupOption


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .product_configurator_setting import ProductConfiguratorSetting  # noqa: E402
from .property_group import PropertyGroup  # noqa: E402
