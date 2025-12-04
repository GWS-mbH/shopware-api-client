from shopware_api_client.fieldsets import FieldSetBase


class QuantityInformation(FieldSetBase):
    max_purchase: int | None = None
    min_purchase: int | None = 1
    purchase_steps: int | None = 1
