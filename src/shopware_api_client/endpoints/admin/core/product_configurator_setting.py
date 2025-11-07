from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_configurator_setting import (
    ProductConfiguratorSetting as ProductConfiguratorSettingBase,
)


class ProductConfiguratorSetting(ProductConfiguratorSettingBase, AdminModel["ProductConfiguratorSettingEndpoint"]):
    product: ForeignRelation["Product"]
    media: ForeignRelation["Media"]
    option: ForeignRelation["PropertyGroupOption"]


class ProductConfiguratorSettingEndpoint(AdminEndpoint[ProductConfiguratorSetting]):
    name = "product_configurator_setting"
    path = "/product-configurator-setting"
    model_class = ProductConfiguratorSetting


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .property_group_option import PropertyGroupOption  # noqa: E402
