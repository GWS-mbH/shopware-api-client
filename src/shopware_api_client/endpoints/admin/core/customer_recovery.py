from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.customer_recovery import CustomerRecoveryBase


class CustomerRecovery(CustomerRecoveryBase, AdminModel["CustomerRecoveryEndpoint"]):
    customer: ForeignRelation["Customer"] = Field(default=...)


class CustomerRecoveryEndpoint(AdminEndpoint[CustomerRecovery]):
    name = "customer_recovery"
    path = "/customer-recovery"
    model_class = CustomerRecovery


from .customer import Customer  # noqa: E402
