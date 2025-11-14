from shopware_api_client.fieldsets import FieldSetBase


class ReferencePriceDefinition(FieldSetBase):
    purchase_unit: float
    reference_unit: float
    unit_name: str
