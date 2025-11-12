from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.b2b_employee import B2bEmployee as B2bEmployeeBase


class B2bEmployee(B2bEmployeeBase, AdminModel["B2bEmployeeEndpoint"]):
    business_partner_customer: ForeignRelation["Customer"]
    role: ForeignRelation["B2bComponentsRole"]
    language: ForeignRelation["Language"]


class B2bEmployeeEndpoint(AdminEndpoint[B2bEmployee]):
    name = "b2b_employee"
    path = "/b2b-employee"
    model_class = B2bEmployee


from .b2b_components_role import B2bComponentsRole  # noqa: E402
from ..core.customer import Customer  # noqa: E402
from ..core.language import Language  # noqa: E402
