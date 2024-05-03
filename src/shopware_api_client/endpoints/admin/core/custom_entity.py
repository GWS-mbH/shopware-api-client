
from pydantic import AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField


class CustomEntityBase(ApiModelBase[EndpointClass]):
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


class CustomEntityRelations:
    pass


class CustomEntity(CustomEntityBase["CustomEntityEndpoint"], CustomEntityRelations):
    pass


class CustomEntityEndpoint(EndpointBase[CustomEntity]):
    name = "custom_entity"
    path = "/custom-entity"
    model_class = CustomEntity
