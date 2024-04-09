from typing import Any

from pydantic import AwareDatetime

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class B2bEmployeeBase(ApiModelBase[EndpointClass]):
    _identifier: str = "b2b_employee"

    business_partner_customer_id: IdField | None = None
    role_id: IdField | None = None
    language_id: IdField
    active: bool | None = None
    first_name: str
    last_name: str
    email: str
    recovery_time: AwareDatetime | None = None
    custom_fields: dict[str, Any] | None = None


class B2bEmployeeRelations:
    business_partner_customer: ForeignRelation["Customer"]
    role: ForeignRelation["B2bComponentsRole"]
    language: ForeignRelation["Language"]


class B2bEmployee(B2bEmployeeBase["B2bEmployeeEndpoint"], B2bEmployeeRelations):
    pass


class B2bEmployeeEndpoint(EndpointBase[B2bEmployee]):
    name = "b2b_employee"
    path = "/b2b-employee"
    model_class = B2bEmployee


from .b2b_components_role import B2bComponentsRole  # noqa: E402
from ..core.customer import Customer  # noqa: E402
from ..core.language import Language  # noqa: E402
