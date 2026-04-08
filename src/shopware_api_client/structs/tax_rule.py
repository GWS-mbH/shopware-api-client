from shopware_api_client.fieldsets import FieldSetBase


class TaxRule(FieldSetBase):
    tax_rate: float
    percentage: float = 100
