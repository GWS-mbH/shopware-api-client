from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class DynamicAccessBase(ApiModelBase):
    _identifier: str = "dynamic_access"

    product_id: Annotated[IdField, RefersTo("product")]
    rule_id: Annotated[IdField, RefersTo("rule")]
