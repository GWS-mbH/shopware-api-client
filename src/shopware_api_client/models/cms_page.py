from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class CmsPageBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "cms_page"

    name: str | None = None
    type: str
    entity: str | None = None
    css_class: str | None = None
    config: dict[str, Any] | None = Field(default=None)
    preview_media_id: IdField | None = None
    locked: bool | None = None
