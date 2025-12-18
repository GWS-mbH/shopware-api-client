from typing import Any
from pydantic import Field
from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class CategoryBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "category"

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
    slot_config: dict[str, Any] | list[Any] | None = Field(default=None)
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
