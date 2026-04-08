from typing import Literal

from .calculated_tax import CalculatedTax
from .tax_rule import TaxRule
from ..fieldsets import FieldSetBase


class CartPrice(FieldSetBase):
    net_price: float
    total_price: float
    position_price: float
    calculated_taxes: list[CalculatedTax] | None = None
    tax_rules: list[TaxRule] | None = None
    tax_status: Literal["gross", "net", "tax-free"]
    raw_total: float
