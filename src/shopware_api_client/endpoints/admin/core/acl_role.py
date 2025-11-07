from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.acl_role import AclRole as AclRoleBase


class AclRole(AclRoleBase, AdminModel["AclRoleEndpoint"]):
    users: ManyRelation["User"]
    app: ForeignRelation["App"]
    integrations: ManyRelation["Integration"]


class AclRoleEndpoint(AdminEndpoint[AclRole]):
    name = "acl_role"
    path = "/acl-role"
    model_class = AclRole


from .app import App  # noqa: E402
from .integration import Integration  # noqa: E402
from .user import User  # noqa: E402
