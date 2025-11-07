from shopware_api_client.fieldsets import FieldSetBase
from shopware_api_client.endpoints.base_fields import IdField


class TaxFreeConfig(FieldSetBase):
    enabled: bool = False
    currency_id: IdField
    amount: float = 0
