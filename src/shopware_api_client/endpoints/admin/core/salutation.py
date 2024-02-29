from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Customer, CustomerAddress, OrderAddress, OrderCustomer


class SalutationBase(ApiModelBase[EndpointClass]):
    _identifier: str = "salutation"

    salutation_key: str = Field(
        ..., serialization_alias="salutationKey", validation_alias=AliasChoices("salutation_key", "salutationKey")
    )
    display_name: str = Field(
        ..., serialization_alias="displayName", validation_alias=AliasChoices("display_name", "displayName")
    )
    letter_name: str = Field(
        ..., serialization_alias="letterName", validation_alias=AliasChoices("letter_name", "letterName")
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
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
    translated: dict[str, Any] | None = None


class SalutationRelations:
    customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "customers")
    customer_addresses: ClassVar[ManyRelation["CustomerAddress"]] = ManyRelation("CustomerAddress", "customerAddresses")
    order_customers: ClassVar[ManyRelation["OrderCustomer"]] = ManyRelation("OrderCustomer", "orderCustomers")
    order_addresses: ClassVar[ManyRelation["OrderAddress"]] = ManyRelation("OrderAddress", "orderAddresses")

    """
    Todo:
    newsletter_recipients[NewsletterRecipient]
    """


class Salutation(SalutationBase["SalutationEndpoint"], SalutationRelations):
    pass


class SalutationEndpoint(EndpointBase[Salutation]):
    name = "salutation"
    path = "/salutation"
    model_class = Salutation


registry.register_admin(SalutationEndpoint)
