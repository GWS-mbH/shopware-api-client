from pydantic import AwareDatetime

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ForeignRelation, ManyRelation


class AclRoleBase(ApiModelBase[EndpointClass]):
    _identifier = "acl_role"

    name: str
    description: str | None = None
    privileges: list[str]
    deleted_at: AwareDatetime | None = None


class AclRoleRelations:
    users: ManyRelation["User"]
    app: ForeignRelation["App"]
    integrations: ManyRelation["Integration"]


class AclRole(AclRoleBase["AclRoleEndpoint"], AclRoleRelations):
    pass


class AclRoleEndpoint(EndpointBase[AclRole]):
    name = "acl_role"
    path = "/acl-role"
    model_class = AclRole


from .app import App  # noqa: E402
from .integration import Integration  # noqa: E402
from .user import User  # noqa: E402
