from typing import Any

from pydantic import Field

from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.fieldsets import FieldSetBase


class Price(FieldSetBase):
    currency_id: IdField
    gross: float
    net: float
    linked: bool
    list_price: "Price | None" = None
    regulation_price: "Price | None" = None
    percentage: list[Any] | dict[str, Any] | None = Field(default=None)
