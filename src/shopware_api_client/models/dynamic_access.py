from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class DynamicAccess(ApiModelBase):
    _identifier: str = "dynamic_access"

    product_id: IdField
    rule_id: IdField
