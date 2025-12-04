from shopware_api_client.fieldsets import FieldSetBase


class ListPrice(FieldSetBase):
    price: float
    discount: float
    percentage: float
