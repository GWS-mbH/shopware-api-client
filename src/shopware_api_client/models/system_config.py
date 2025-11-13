from typing import Any

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class SystemConfigBase(ApiModelBase):
    _identifier: str = "system_config"

    configuration_key: str
    configuration_value: Any
    sales_channel_id: IdField | None = None
