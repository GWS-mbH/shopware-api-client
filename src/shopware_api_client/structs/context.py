from typing import Any

from shopware_api_client.fieldsets import FieldSetBase


class Context(FieldSetBase):
    version_id: str | None = None
    currency_id: str | None = None
    currency_factor: int | None = None
    currency_precision: int | None = None
    language_id_chain: list[str] | None = None
    scope: str | None = None
    source: dict[str, Any] | None = None
    tax_state: str | None = None
    use_cache: bool | None = None
