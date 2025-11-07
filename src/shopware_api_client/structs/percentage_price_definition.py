from shopware_api_client.fieldsets import FieldSetBase


class PercentagePriceDefinition(FieldSetBase):
    type: str = "percentage"
    percentage: float
