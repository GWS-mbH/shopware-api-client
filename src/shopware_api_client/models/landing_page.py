from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class LandingPageBase(ApiModelBase, CustomFieldsMixin):
    active: bool | None = None
    name: str
    slot_config: dict[str, Any] | None = Field(default=None)
    meta_title: str | None = None
    meta_description: str | None = None
    keywords: str | None = None
    url: str
    cms_page_id: IdField | None = None
    cms_page_version_id: IdField | None = None
