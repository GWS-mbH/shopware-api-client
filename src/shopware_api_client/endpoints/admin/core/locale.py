from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.locale import LocaleBase


class Locale(LocaleBase, AdminModel["LocaleEndpoint"]):
    languages: ManyRelation["Language"] = Field(default=...)
    users: ManyRelation["User"] = Field(default=...)


class LocaleEndpoint(AdminEndpoint[Locale]):
    name = "locale"
    path = "/locale"
    model_class = Locale


from .language import Language  # noqa: E402
from .user import User  # noqa: E402
