from .calculated_tax import CalculatedTax
from .list_price import ListPrice
from .reference_price import ReferencePrice
from .regulation_price import RegulationPrice
from .tax_rule import TaxRule
from ..fieldsets import FieldSetBase


class CalculatedPrice(FieldSetBase):
    unit_price: float
    total_price: float
    calculated_taxes: list[CalculatedTax] | None = None
    tax_rules: list[TaxRule] | None = None
    quantity: int = 1
    reference_price: ReferencePrice | None = None
    list_price: ListPrice | None = None
    regulation_price: RegulationPrice | None = None
