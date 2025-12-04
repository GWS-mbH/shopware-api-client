from shopware_api_client.fieldsets import FieldSetBase


class CalculatedTax(FieldSetBase):
    tax: float = 0
    tax_rate: float
    price: float = 0
    label: str | None = None
