from pydantic import AwareDatetime
from shopware_api_client.base import ApiModelBase


class AclRole(ApiModelBase):
    _identifier = "acl_role"

    name: str
    description: str | None = None
    privileges: list[str]
    deleted_at: AwareDatetime | None = None
