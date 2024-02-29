from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Language, User


class LocaleBase(ApiModelBase[EndpointClass]):
    _identifier: str = "locale"

    code: str
    name: str
    territory: str
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
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
    translated: dict[str, Any] | None = None


class LocaleRelations:
    languages: ClassVar[ManyRelation["Language"]] = ManyRelation("Language", "languages")
    users: ClassVar[ManyRelation["User"]] = ManyRelation("User", "users")


class Locale(LocaleBase["LocaleEndpoint"], LocaleRelations):
    pass


class LocaleEndpoint(EndpointBase[Locale]):
    name = "locale"
    path = "/locale"
    model_class = Locale


registry.register_admin(LocaleEndpoint)
