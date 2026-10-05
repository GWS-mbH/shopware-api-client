from typing import Annotated, Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class LandingPageBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "landing_page"

    active: bool | None = None
    name: str
    slot_config: dict[str, Any] | None = Field(default=None)
    meta_title: str | None = None
    meta_description: str | None = None
    keywords: str | None = None
    url: str
    cms_page_id: Annotated[IdField | None, RefersTo("cms_page")] = None
    cms_page_version_id: IdField | None = None
