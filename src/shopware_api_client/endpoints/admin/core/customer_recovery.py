from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class CustomerRecoveryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer_recovery"

    hash: str
    customer_id: IdField


class CustomerRecoveryRelations:
    customer: ForeignRelation["Customer"]


class CustomerRecovery(CustomerRecoveryBase["CustomerRecoveryEndpoint"], CustomerRecoveryRelations):
    pass


class CustomerRecoveryEndpoint(EndpointBase[CustomerRecovery]):
    name = "customer_recovery"
    path = "/customer-recovery"
    model_class = CustomerRecovery


from .customer import Customer  # noqa: E402
