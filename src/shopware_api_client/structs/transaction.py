from .calculated_price import CalculatedPrice
from ..endpoints.base_fields import IdField
from ..fieldsets import FieldSetBase


class Transaction(FieldSetBase):
    payment_method_id: IdField | None = None
    amount: CalculatedPrice | None = None
