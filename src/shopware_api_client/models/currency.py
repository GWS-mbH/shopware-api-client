from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class CurrencyBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "currency"

    factor: float
    symbol: str
    iso_code: str
    short_name: str
    name: str
    position: int | None = None
    is_system_default: bool | None = Field(
        None,
        description="Runtime field, cannot be used as part of the criteria.",
    )
    tax_free_from: float | None = None

