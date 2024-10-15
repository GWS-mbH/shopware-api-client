from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class SystemConfigBase(ApiModelBase[EndpointClass]):
    _identifier: str = "system_config"

    configuration_key: str
    configuration_value: Any
    sales_channel_id: IdField | None = None


class SystemConfigRelations:
    sales_channel: ForeignRelation["SalesChannel"]


class SystemConfig(SystemConfigBase["SystemConfigEndpoint"], SystemConfigRelations):
    pass


class SystemConfigEndpoint(EndpointBase[SystemConfig]):
    name = "system_config"
    path = "/system-config"
    model_class = SystemConfig


from .sales_channel import SalesChannel  # noqa: E402
