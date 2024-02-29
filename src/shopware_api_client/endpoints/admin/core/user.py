from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Customer, Locale, Media, Order, StateMachineHistory


class UserBase(ApiModelBase[EndpointClass]):
    _identifier: str = "user"

    locale_id: IdField = Field(
        ..., serialization_alias="localeId", validation_alias=AliasChoices("locale_id", "localeId")
    )
    username: str
    first_name: str = Field(
        ..., serialization_alias="firstName", validation_alias=AliasChoices("first_name", "firstName")
    )
    last_name: str = Field(..., serialization_alias="lastName", validation_alias=AliasChoices("last_name", "lastName"))
    title: str | None = None
    email: str
    active: bool | None = None
    admin: bool | None = None
    last_updated_password_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="lastUpdatedPasswordAt",
        validation_alias=AliasChoices("last_updated_password_at", "lastUpdatedPasswordAt"),
    )
    time_zone: str = Field(..., serialization_alias="timeZone", validation_alias=AliasChoices("time_zone", "timeZone"))
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    avatar_id: IdField | None = Field(
        default=None, serialization_alias="avatarId", validation_alias=AliasChoices("avatar_id", "avatarId")
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class UserRelations:
    locale: ClassVar[ForeignRelation["Locale"]] = ForeignRelation("Locale", "locale_id")
    avatar_media: ClassVar[ManyRelation["Media"]] = ManyRelation("Media", "avatarMedia")
    media: ClassVar[ManyRelation["Media"]] = ManyRelation("Media", "media")
    state_machine_history_entries: ClassVar[ManyRelation["StateMachineHistory"]] = ManyRelation(
        "StateMachineHistory", "stateMachineHistoryEntries"
    )
    created_orders: ClassVar[ManyRelation["Order"]] = ManyRelation("Order", "createdOrders")
    updated_orders: ClassVar[ManyRelation["Order"]] = ManyRelation("Order", "updatedOrders")
    created_customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "created-customers")
    updated_customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "updated-customers")

    """
    Todo:
    access_keys[UserAccessKey], configs[UserConfig], import_export_log_entries[ImportExportLog], acl_roles[AclRole],
    recovery_user[UserRecovery]
    """


class User(UserBase["UserEndpoint"], UserRelations):
    pass


class UserEndpoint(EndpointBase[User]):
    name = "user"
    path = "/user"
    model_class = User


registry.register_admin(UserEndpoint)
