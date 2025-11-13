from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class CustomerRecoveryBase(ApiModelBase):
    _identifier: str = "customer_recovery"

    hash: str
    customer_id: IdField
