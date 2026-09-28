from typing import Annotated

from .calculated_price import CalculatedPrice
from ..endpoints.base_fields import IdField, RefersTo
from ..fieldsets import FieldSetBase


class Transaction(FieldSetBase):
    payment_method_id: Annotated[IdField | None, RefersTo("payment_method")] = None
    amount: CalculatedPrice | None = None
