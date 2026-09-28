from typing import Annotated

from shopware_api_client.fieldsets import FieldSetBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class TaxFreeConfig(FieldSetBase):
    enabled: bool = False
    currency_id: Annotated[IdField, RefersTo("currency")]
    amount: float = 0
