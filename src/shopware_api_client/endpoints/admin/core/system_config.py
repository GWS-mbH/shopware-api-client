from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.system_config import SystemConfigBase


class SystemConfig(SystemConfigBase, AdminModel["SystemConfigEndpoint"]):
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)


class SystemConfigEndpoint(AdminEndpoint[SystemConfig]):
    name = "system_config"
    path = "/system-config"
    model_class = SystemConfig


from .sales_channel import SalesChannel  # noqa: E402
