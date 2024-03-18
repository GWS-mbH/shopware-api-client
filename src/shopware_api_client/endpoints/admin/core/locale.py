from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class LocaleBase(ApiModelBase[EndpointClass]):
    _identifier: str = "locale"

    code: str
    name: str
    territory: str
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class LocaleRelations:
    languages: ManyRelation["Language"]
    users: ManyRelation["User"]


class Locale(LocaleBase["LocaleEndpoint"], LocaleRelations):
    pass


class LocaleEndpoint(EndpointBase[Locale]):
    name = "locale"
    path = "/locale"
    model_class = Locale


from .language import Language  # noqa: E402
from .user import User  # noqa: E402
