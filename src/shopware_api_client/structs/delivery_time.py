from shopware_api_client.fieldsets import FieldSetBase


class DeliveryTime(FieldSetBase):
    name: str | None = None
    min: int | None = None
    max: int | None = None
    unit: str | None = None
