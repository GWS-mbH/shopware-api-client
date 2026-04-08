from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.integration import IntegrationBase


class Integration(IntegrationBase, AdminModel["IntegrationEndpoint"]):
    app: ForeignRelation["App"] = Field(default=...)
    acl_roles: ManyRelation["AclRole"] = Field(default=...)


class IntegrationEndpoint(AdminEndpoint[Integration]):
    name = "integration"
    path = "/integration"
    model_class = Integration


from .acl_role import AclRole  # noqa: E402
from .app import App  # noqa: E402
