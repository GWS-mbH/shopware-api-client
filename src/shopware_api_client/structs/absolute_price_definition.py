from shopware_api_client.fieldsets import FieldSetBase


class AbsolutePriceDefinition(FieldSetBase):
    type: str = "absolute"
    price: float | None = None
