from shopware_api_client.base import StoreSearchEndpoint, EndpointMixin
from shopware_api_client.models.language import LanguageBase


class Language(LanguageBase, EndpointMixin["LanguageEndpoint"]):
    parent: "Language | None" = None
    locale: "Locale | None" = None
    translation_code: "Locale | None" = None
    children: list["Language"] | None = None


class LanguageEndpoint(StoreSearchEndpoint[Language]):
    model_class = Language
    name = "language"
    path = "/language"


from .locale import Locale  # noqa: E402
