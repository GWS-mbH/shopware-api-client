from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class AppBase(ApiModelBase[EndpointClass]):
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
    modules: list[dict[str, Any]] | None = None
    main_module: dict[str, Any] | None = None
    cookies: list[dict[str, Any]] | None = None
    allow_disable: bool
    base_app_url: str | None = None
    allowed_hosts: list[str] | None = None
    template_load_priority: int | None = None
    label: str
    description: str | None = None
    privacy_policy_extensions: str | None = None
    custom_fields: dict[str, Any] | None = None
    integration_id: IdField
    acl_role_id: IdField
    translated: dict[str, Any] | None = None


class AppRelations:
    app: ForeignRelation["App"]
    acl_roles: ManyRelation["AclRole"]
    integrations: ManyRelation["Integration"]


class App(AppBase["AppEndpoint"], AppRelations):
    pass


class AppEndpoint(EndpointBase[App]):
    name = "app"
    path = "/app"
    model_class = App


from .acl_role import AclRole  # noqa: E402
from .app import App  # noqa: E402
from .integration import Integration  # noqa: E402
