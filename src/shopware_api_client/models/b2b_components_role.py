from typing import Any

from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class B2bComponentsRoleBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "b2b_components_role"

    business_partner_customer_id: IdField | None = None
    name: str
    permissions: dict[str, Any] | None = Field(default=None)
