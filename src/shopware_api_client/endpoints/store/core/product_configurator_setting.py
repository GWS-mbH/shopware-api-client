from shopware_api_client.models.product_configurator_setting import ProductConfiguratorSettingBase


class ProductConfiguratorSetting(ProductConfiguratorSettingBase):
    media: "Media | None" = None
    option: "PropertyGroupOption | None" = None


from .media import Media  # noqa: E402
from .property_group_option import PropertyGroupOption  # noqa: E402
