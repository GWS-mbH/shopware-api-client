from typing import Any
from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class ProductConfiguratorSettingBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_configurator_setting"

    product_id: IdField
    product_version_id: IdField | None = None
    media_id: IdField | None = None
    option_id: IdField
    price: dict[str, Any] | None = None
    position: int | None = None
