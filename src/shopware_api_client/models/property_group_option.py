from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class PropertyGroupOptionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "property_group_option"

    group_id: Annotated[IdField | None, RefersTo("property_group")] = None
    name: str | None = None
    position: int | None = None
    color_hex_code: str | None = None
    media_id: Annotated[IdField | None, RefersTo("media")] = None
