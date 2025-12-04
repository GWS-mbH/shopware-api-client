from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class CustomEntityBase(ApiModelBase):
    _identifier: str = "custom_entity"

    name: str
    fields: list
    flags: list | None = None
    app_id: IdField | None = None
    plugin_id: IdField | None = None
    cms_aware: bool | None = None
    store_api_aware: bool | None = None
    custom_fields_aware: bool | None = None
    label_property: str | None = None
    deleted_at: AwareDatetime | None = Field(default=None)
