from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductConfiguratorSettingBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_configurator_setting"

    version_id: IdField | None = None
    product_id: IdField
    product_version_id: IdField | None = None
    media_id: IdField | None = None
    option_id: IdField
    price: dict[str, Any] | None = None
    position: int | None = None
    custom_fields: dict[str, Any] | None = None


class ProductConfiguratorSettingRelations:
    product: ForeignRelation["Product"]
    media: ForeignRelation["Media"]
    option: ForeignRelation["PropertyGroupOption"]


class ProductConfiguratorSetting(
    ProductConfiguratorSettingBase["ProductConfiguratorSettingEndpoint"], ProductConfiguratorSettingRelations
):
    pass


class ProductConfiguratorSettingEndpoint(EndpointBase[ProductConfiguratorSetting]):
    name = "product_configurator_setting"
    path = "/product-configurator-setting"
    model_class = ProductConfiguratorSetting


from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .property_group_option import PropertyGroupOption  # noqa: E402
