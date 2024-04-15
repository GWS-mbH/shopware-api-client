from typing import Any

from pydantic import AwareDatetime

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ForeignRelation, ManyRelation


class IntegrationBase(ApiModelBase[EndpointClass]):
    _identifier = "integration"

    label: str
    access_key: str
    secret_access_key: str
    last_usage_at: AwareDatetime | None = None
    admin: bool | None = None
    custom_fields: dict[str, Any] | None = None
    deleted_at: AwareDatetime | None = None
    write_access: bool | None = None


class IntegrationRelations:
    app: ForeignRelation["App"]
    acl_roles: ManyRelation["AclRole"]


class Integration(IntegrationBase["IntegrationEndpoint"], IntegrationRelations):
    pass


class IntegrationEndpoint(EndpointBase[Integration]):
    name = "integration"
    path = "/integration"
    model_class = Integration


from .acl_role import AclRole  # noqa: E402
from .app import App  # noqa: E402
