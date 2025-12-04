from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.user import UserBase


class User(UserBase, AdminModel["UserEndpoint"]):
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


class UserEndpoint(AdminEndpoint[User]):
    name = "user"
    path = "/user"
    model_class = User


from .acl_role import AclRole  # noqa: E402
from .customer import Customer  # noqa: E402
from .locale import Locale  # noqa: E402
from .media import Media  # noqa: E402
from .order import Order  # noqa: E402
from .state_machine_history import StateMachineHistory  # noqa: E402
