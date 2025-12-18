from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_configurator_setting import ProductConfiguratorSettingBase


class ProductConfiguratorSetting(ProductConfiguratorSettingBase, AdminModel["ProductConfiguratorSettingEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    media: ForeignRelation["Media"] = Field(default=...)
    option: ForeignRelation["PropertyGroupOption"] = Field(default=...)


class ProductConfiguratorSettingEndpoint(AdminEndpoint[ProductConfiguratorSetting]):
    name = "product_configurator_setting"
    path = "/product-configurator-setting"
    model_class = ProductConfiguratorSetting


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .property_group_option import PropertyGroupOption  # noqa: E402
