from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class CategoryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "category"

    version_id: IdField | None = None
    parent_id: IdField | None = None
    parent_version_id: IdField | None = None
    after_category_id: IdField | None = None
    after_category_version_id: IdField | None = None
    media_id: IdField | None = None
    display_nested_products: bool
    auto_increment: int | None = Field(default=None, exclude=True)
    breadcrumb: list[str] | None = Field(default=None, exclude=True)
    level: int | None = Field(default=None, exclude=True)
    path: str | None = Field(default=None, exclude=True)
    child_count: int | None = Field(default=None, exclude=True)
    type: str
    product_assignment_type: str
    visible: bool | None = None
    active: bool | None = None
    cms_page_id_sIdFieldched: bool | None = Field(
        default=None, description="Runtime field, cannot be used as part of the criteria."
    )
    visible_child_count: int | None = Field(
        default=None, description="Runtime field, cannot be used as part of the criteria."
    )
    name: str
    custom_fields: dict[str, Any] | None = None
    slot_config: dict[str, Any] | list[Any] | None = None
    link_type: str | None = None
    internal_link: str | None = None
    external_link: str | None = None
    link_new_tab: bool | None = None
    description: str | None = None
    meta_title: str | None = None
    meta_description: str | None = None
    keywords: str | None = None
    cms_page_id: IdField | None = None
    cms_page_version_id: IdField | None = None
    product_stream_id: IdField | None = None
    custom_entity_type_id: IdField | None = None
    translated: dict[str, Any] | None = None


class CategoryRelations:
    parent: ForeignRelation["Category"]
    children: ManyRelation["Category"]
    media: ForeignRelation["Media"]
    products: ManyRelation["Product"]
    nested_products: ManyRelation["Product"]
    tags: ManyRelation["Tag"]
    cms_page: ForeignRelation["CmsPage"]
    product_stream: ForeignRelation["ProductStream"]
    navigation_sales_channels: ManyRelation["SalesChannel"]
    footer_sales_channels: ManyRelation["SalesChannel"]
    service_sales_channels: ManyRelation["SalesChannel"]
    main_categories: ManyRelation["MainCategory"]
    seo_urls: ManyRelation["SeoUrl"]


class Category(CategoryBase["CategoryEndpoint"], CategoryRelations):
    pass


class CategoryEndpoint(EndpointBase[Category]):
    name = "category"
    path = "/category"
    model_class = Category


from .cms_page import CmsPage  # noqa: E402
from .main_category import MainCategory  # noqa: E402
from .media import Media  # noqa: E402
from .product import Product  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .seo_url import SeoUrl  # noqa: E402
from .tag import Tag  # noqa: E402
