from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class SeoUrlBase(ApiModelBase[EndpointClass]):
    _identifier: str = "seo_url"

    sales_channel_id: IdField | None = None
    language_id: IdField
    foreign_key: IdField
    route_name: str
    path_info: str
    seo_path_info: str
    is_canonical: bool | None = None
    is_modified: bool | None = None
    is_deleted: bool | None = None
    url: str | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")
    custom_fields: dict[str, Any] | None = None
    is_valid: bool | None = Field(default=None, description="Runtime field, cannot be used as part of the criteria.")


class SeoUrlRelations:
    language: ForeignRelation["Language"]
    sales_channel: ForeignRelation["SalesChannel"]


class SeoUrl(SeoUrlBase["SeoUrlEndpoint"], SeoUrlRelations):
    pass


class SeoUrlEndpoint(EndpointBase[SeoUrl]):
    name = "seo_url"
    path = "/seo-url"
    model_class = SeoUrl


from .language import Language  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
