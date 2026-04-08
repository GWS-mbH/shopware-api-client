from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.b2b_components_role import B2bComponentsRoleBase


class B2bComponentsRole(B2bComponentsRoleBase, AdminModel["B2bComponentsRoleEndpoint"]):
    employees: ManyRelation["B2bEmployee"] = Field(default=...)
    business_partner_customer: ForeignRelation["Customer"] = Field(default=...)


class B2bComponentsRoleEndpoint(AdminEndpoint[B2bComponentsRole]):
    name = "b2b_components_role"
    path = "/b2b-components-role"
    model_class = B2bComponentsRole


from .b2b_employee import B2bEmployee  # noqa: E402
from ..core.customer import Customer  # noqa: E402
