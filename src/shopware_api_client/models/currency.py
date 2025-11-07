from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class Currency(ApiModelBase, CustomFieldsMixin):
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


#    item_rounding: "Rounding"
#    total_rounding: "Rounding"


# from shopware_api_client.endpoints.base_fields import Rounding  # noqa: E402
