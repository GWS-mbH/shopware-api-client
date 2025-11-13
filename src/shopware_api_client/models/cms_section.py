from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, Visibility


class CmsSectionBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "cms_section"

    position: int
    type: str
    locked: bool | None = None
    name: str | None = None
    sizing_mode: str | None = None
    mobile_behavior: str | None = None
    background_color: str | None = None
    background_media_id: IdField | None = None
    background_media_mode: str | None = None
    css_class: str | None = None
    page_id: IdField
    visibility: Visibility | None = None
    cms_page_version_id: IdField | None = None
