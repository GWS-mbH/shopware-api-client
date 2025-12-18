from shopware_api_client.fieldsets import FieldSetBase


class AbsolutPriceDefinition(FieldSetBase):
    type: str = "absolute"
    price: float | None = None
