from shopware_api_client.fieldsets import FieldSetBase


class ReferencePriceDefinition(FieldSetBase):
    purchase_unit: float | None = None
    reference_unit: float | None = None
    unit_name: str | None = None
