from typing import Any

from pydantic import AwareDatetime

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class UserBase(ApiModelBase[EndpointClass]):
    _identifier: str = "user"

    locale_id: IdField
    username: str
    first_name: str
    last_name: str
    password: str | None = None
    title: str | None = None
    email: str
    active: bool | None = None
    admin: bool | None = None
    last_updated_password_at: AwareDatetime | None = None
    time_zone: str
    custom_fields: dict[str, Any] | None = None
    avatar_id: IdField | None = None


class UserRelations:
    locale: ForeignRelation["Locale"]
    avatar_media: ManyRelation["Media"]
    media: ManyRelation["Media"]
    state_machine_history_entries: ManyRelation["StateMachineHistory"]
    created_orders: ManyRelation["Order"]
    updated_orders: ManyRelation["Order"]
    created_customers: ManyRelation["Customer"]
    updated_customers: ManyRelation["Customer"]
    acl_roles: ManyRelation["AclRole"]

    """
    Todo:
    access_keys[UserAccessKey], configs[UserConfig], import_export_log_entries[ImportExportLog],
    recovery_user[UserRecovery]
    """


class User(UserBase["UserEndpoint"], UserRelations):
    pass


class UserEndpoint(EndpointBase[User]):
    name = "user"
    path = "/user"
    model_class = User


from .acl_role import AclRole  # noqa: E402
from .customer import Customer  # noqa: E402
from .locale import Locale  # noqa: E402
from .media import Media  # noqa: E402
from .order import Order  # noqa: E402
from .state_machine_history import StateMachineHistory  # noqa: E402
