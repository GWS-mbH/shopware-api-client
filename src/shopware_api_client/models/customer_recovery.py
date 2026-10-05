from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class CustomerRecoveryBase(ApiModelBase):
    _identifier: str = "customer_recovery"

    hash: str
    customer_id: Annotated[IdField, RefersTo("customer")]
