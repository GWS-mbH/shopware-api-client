from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class B2bComponentsRoleBase(ApiModelBase[EndpointClass]):
    _identifier: str = "b2b_components_role"

    business_partner_customer_id: IdField | None = None
    name: str
    permissions: dict[str, Any] | None = None
    custom_fields: dict[str, Any] | None = None


class B2bComponentsRoleRelations:
    employees: ManyRelation["B2bEmployee"]
    business_partner_customer: ForeignRelation["Customer"]


class B2bComponentsRole(B2bComponentsRoleBase["B2bComponentsRoleEndpoint"], B2bComponentsRoleRelations):
    pass


class B2bComponentsRoleEndpoint(EndpointBase[B2bComponentsRole]):
    name = "b2b_components_role"
    path = "/b2b-components-role"
    model_class = B2bComponentsRole


from .b2b_employee import B2bEmployee  # noqa: E402
from ..core.customer import Customer  # noqa: E402
