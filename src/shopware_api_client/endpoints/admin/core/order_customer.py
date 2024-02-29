from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Customer, Order, Salutation


class OrderCustomerBase(ApiModelBase[EndpointClass]):
    _identifier: str = "language"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    customer_id: IdField | None = Field(
        default=None, serialization_alias="customerId", validation_alias=AliasChoices("customer_id", "customerId")
    )
    order_id: IdField = Field(..., serialization_alias="orderId", validation_alias=AliasChoices("order_id", "orderId"))
    order_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderVersionId",
        validation_alias=AliasChoices("order_version_id", "orderVersionId"),
    )
    email: str
    salutation_id: IdField | None = Field(
        default=None, serialization_alias="salutationId", validation_alias=AliasChoices("salutation_id", "salutationId")
    )
    first_name: str = Field(
        ..., serialization_alias="firstName", validation_alias=AliasChoices("first_name", "firstName")
    )
    last_name: str = Field(..., serialization_alias="lastName", validation_alias=AliasChoices("last_name", "lastName"))
    company: str | None = None
    title: str | None = None
    vat_ids: list[str] | None = Field(
        default=None, serialization_alias="vatIds", validation_alias=AliasChoices("vat_ids", "vatIds")
    )
    customer_number: str | None = Field(
        default=None,
        serialization_alias="customerNumber",
        validation_alias=AliasChoices("customer_number", "customerNumber"),
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    remote_address: str | None = Field(
        default=None,
        serialization_alias="remoteAddress",
        validation_alias=AliasChoices("remote_address", "remoteAddress"),
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


class OrderCustomerRelations:
    order: ClassVar[ForeignRelation["Order"]] = ForeignRelation("Order", "order_id")
    customer: ClassVar[ForeignRelation["Customer"]] = ForeignRelation("Customer", "customer_id")
    salutation: ClassVar[ForeignRelation["Salutation"]] = ForeignRelation("Salutation", "salutation_id")


class OrderCustomer(OrderCustomerBase["OrderCustomerEndpoint"], OrderCustomerRelations):
    pass


class OrderCustomerEndpoint(EndpointBase[OrderCustomer]):
    name = "order_customer"
    path = "/order-customer"
    model_class = OrderCustomer


registry.register_admin(OrderCustomerEndpoint)
