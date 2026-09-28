from typing import Annotated, Any
from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductConfiguratorSettingBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_configurator_setting"

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    media_id: Annotated[IdField | None, RefersTo("media")] = None
    option_id: Annotated[IdField, RefersTo("property_group_option")]
    price: dict[str, Any] | None = None
    position: int | None = None
