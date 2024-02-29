from typing import TYPE_CHECKING, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Customer


class CustomerRecoveryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer_recovery"

    hash: str
    customer_id: IdField = Field(
        ..., serialization_alias="customerId", validation_alias=AliasChoices("customer_id", "customerId")
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None,
        serialization_alias="updatedAt",
        validation_alias=AliasChoices("updated_at", "updatedAt"),
        exclude=True,
    )


class CustomerRecoveryRelations:
    customer: ClassVar[ForeignRelation["Customer"]] = ForeignRelation("Customer", "customer_id")


class CustomerRecovery(CustomerRecoveryBase["CustomerRecoveryEndpoint"], CustomerRecoveryRelations):
    pass


class CustomerRecoveryEndpoint(EndpointBase[CustomerRecovery]):
    name = "customer_recovery"
    path = "/customer-recovery"
    model_class = CustomerRecovery


registry.register_admin(CustomerRecoveryEndpoint)
