from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class CmsPageBase(ApiModelBase[EndpointClass]):
    _identifier: str = "cms_page"

    version_id: IdField | None = None
    name: str | None = None
    type: str
    entity: str | None = None
    css_class: str | None = None
    config: dict[str, Any] | None = None
    preview_media_id: IdField | None = None
    custom_fields: dict[str, Any] | None = None
    locked: bool | None = None
    translated: dict[str, Any] | None = None


class CmsPageRelations:
    sections: ManyRelation["CmsSection"]
    preview_media: ForeignRelation["Media"]
    categories: ManyRelation["Category"]
    landing_pages: ManyRelation["LandingPage"]
    home_sales_channels: ManyRelation["SalesChannel"]
    products: ManyRelation["Product"]


class CmsPage(CmsPageBase["CmsPageEndpoint"], CmsPageRelations):
    pass


class CmsPageEndpoint(EndpointBase[CmsPage]):
    name = "cms_page"
    path = "/cms-page"
    model_class = CmsPage


from .category import Category  # noqa: E402
from .cms_section import CmsSection  # noqa: E402
from .landing_page import LandingPage  # noqa: E402
from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
