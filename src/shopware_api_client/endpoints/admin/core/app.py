from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.app import AppBase


class App(AppBase, AdminModel["AppEndpoint"]):
    app: ForeignRelation["App"] = Field(default=...)
    acl_roles: ManyRelation["AclRole"] = Field(default=...)
    integrations: ManyRelation["Integration"] = Field(default=...)


class AppEndpoint(AdminEndpoint[App]):
    name = "app"
    path = "/app"
    model_class = App


from .acl_role import AclRole  # noqa: E402
from .app import App  # noqa: E402
from .integration import Integration  # noqa: E402
