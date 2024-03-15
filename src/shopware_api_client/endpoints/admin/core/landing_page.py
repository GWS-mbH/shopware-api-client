from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class LandingPageBase(ApiModelBase[EndpointClass]):
    _identifier: str = "landing_page"

    version_id: IdField | None = None
    active: bool | None = None
    name: str
    custom_fields: dict[str, Any] | None = None
    slot_config: dict[str, Any] | None = None
    meta_title: str | None = None
    meta_description: str | None = None
    keywords: str | None = None
    url: str
    cms_page_id: IdField | None = None
    cms_page_version_id: IdField | None = None
    translated: dict[str, Any] | None = None


class LandingPageRelations:
    tags: ManyRelation["Tag"]
    cms_page: ForeignRelation["CmsPage"]
    sales_channels: ManyRelation["SalesChannel"]
    seo_urls: ManyRelation["SeoUrl"]


class LandingPage(LandingPageBase["LandingPageEndpoint"], LandingPageRelations):
    pass


class LandingPageEndpoint(EndpointBase[LandingPage]):
    name = "landing_page"
    path = "/landing-page"
    model_class = LandingPage


from .cms_page import CmsPage  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .tag import Tag  # noqa: E402
