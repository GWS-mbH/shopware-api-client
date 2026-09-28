from typing import Annotated

from pydantic import Field
from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class SeoUrlBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "seo_url"

    sales_channel_id: Annotated[IdField | None, RefersTo("sales_channel")] = None
    language_id: Annotated[IdField, RefersTo("language")]
    foreign_key: IdField
    route_name: str
    path_info: str
    seo_path_info: str
    is_canonical: bool | None = None
    is_modified: bool | None = None
    is_deleted: bool | None = None
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    is_valid: bool | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
