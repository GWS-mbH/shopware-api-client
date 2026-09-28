from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo, Visibility


class CmsBlockBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "cms_block"

    position: int
    type: str
    locked: bool | None = None
    name: str | None = None
    section_position: str | None = None
    margin_top: str | None = None
    margin_bottom: str | None = None
    margin_left: str | None = None
    margin_right: str | None = None
    background_color: str | None = None
    background_media_id: Annotated[IdField | None, RefersTo("media")] = None
    background_media_mode: str | None = None
    css_class: str | None = None
    visibility: Visibility | None = None
    section_id: Annotated[IdField, RefersTo("cms_section")]
    cms_section_version_id: IdField | None = None
