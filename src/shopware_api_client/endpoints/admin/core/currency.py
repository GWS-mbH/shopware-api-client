from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Rounding
from ...relations import ManyRelation


class CurrencyBase(ApiModelBase[EndpointClass]):
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
    custom_fields: dict[str, Any] | None = None
    item_rounding: Rounding
    total_rounding: Rounding
    translated: dict[str, Any] | None = None


class CurrencyRelations:
    sales_channel_default_assignments: ManyRelation["SalesChannel"]
    orders: ManyRelation["Order"]
    sales_channels: ManyRelation["SalesChannel"]
    sales_channel_domains: ManyRelation["SalesChannelDomain"]
    promotion_discount_prices: ManyRelation["PromotionDiscountPrices"]
    product_exports: ManyRelation["ProductExport"]
    country_roundings: ManyRelation["CurrencyCountryRounding"]


class Currency(CurrencyBase["CurrencyEndpoint"], CurrencyRelations):
    pass


class CurrencyEndpoint(EndpointBase[Currency]):
    name = "currency"
    path = "/currency"
    model_class = Currency


from .currency_country_rounding import CurrencyCountryRounding  # noqa: E402
from .order import Order  # noqa: E402
from .product_export import ProductExport  # noqa: E402
from .promotion_discount_prices import PromotionDiscountPrices  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .sales_channel_domain import SalesChannelDomain  # noqa: E402
