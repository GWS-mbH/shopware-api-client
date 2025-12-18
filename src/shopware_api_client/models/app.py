from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class AppBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "app"

    name: str
    path: str
    author: str | None = None
    copyright: str | None = None
    license: str | None = None
    active: bool
    configurable: bool
    privacy: str | None = None
    version: str
    icon: str | None = Field(None, description="Runtime field, cannot be used as part of the criteria.", exclude=True)
    modules: list[dict[str, Any]] | None = Field(default=None)
    main_module: dict[str, Any] | None = Field(default=None)
    cookies: list[dict[str, Any]] | None = Field(default=None)
    allow_disable: bool
    base_app_url: str | None = None
    allowed_hosts: list[str] | None = Field(default=None)
    template_load_priority: int | None = None
    label: str
    description: str | None = None
    privacy_policy_extensions: str | None = None
    integration_id: IdField
    acl_role_id: IdField
