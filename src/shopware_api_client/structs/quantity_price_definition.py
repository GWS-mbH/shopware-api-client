from .reference_price_definition import ReferencePriceDefinition
from .tax_rule import TaxRule
from ..fieldsets import FieldSetBase


class QuantityPriceDefinition(FieldSetBase):
    type: str = "quantitiy"
    is_calculated: bool = True
    reference_price_definition: ReferencePriceDefinition | None = None
    list_price: float | None = None
    regulation_price: float | None = None
    price: float | None = None
    tax_rules: list[TaxRule] | None = None
    quantity: int = 1
