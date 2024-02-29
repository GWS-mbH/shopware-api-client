from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Country, CountryState, Customer, Salutation


class CustomerAddressBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer_address"

    customer_id: IdField = Field(
        ..., serialization_alias="customerId", validation_alias=AliasChoices("customer_id", "customerId")
    )
    country_id: IdField = Field(
        ..., serialization_alias="countryId", validation_alias=AliasChoices("country_id", "countryId")
    )
    country_state_id: IdField | None = Field(
        default=None,
        serialization_alias="countryStateId",
        validation_alias=AliasChoices("country_state_id", "countryStateId"),
    )
    salutation_id: IdField | None = Field(
        default=None, serialization_alias="salutationId", validation_alias=AliasChoices("salutation_id", "salutationId")
    )
    first_name: str = Field(
        ..., serialization_alias="firstName", validation_alias=AliasChoices("first_name", "firstName")
    )
    last_name: str = Field(..., serialization_alias="lastName", validation_alias=AliasChoices("last_name", "lastName"))
    zipcode: str | None = None
    city: str
    company: str | None = None
    street: str
    department: str | None = None
    title: str | None = None
    phone_number: str | None = Field(
        default=None, serialization_alias="phoneNumber", validation_alias=AliasChoices("phone_number", "phoneNumber")
    )
    additional_address_line1: str | None = Field(
        default=None,
        serialization_alias="additionalAddressLine1",
        validation_alias=AliasChoices("additional_address_line1", "additionalAddressLine1"),
    )
    additional_address_line2: str | None = Field(
        default=None,
        serialization_alias="additionalAddressLine2",
        validation_alias=AliasChoices("additional_address_line2", "additionalAddressLine2"),
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


class CustomerAddressRelations:
    customer: ClassVar[ForeignRelation["Customer"]] = ForeignRelation("Customer", "customer_id")
    country: ClassVar[ForeignRelation["Country"]] = ForeignRelation("Country", "country_id")
    country_state: ClassVar[ForeignRelation["CountryState"]] = ForeignRelation("CountryState", "country_state_id")
    salutation: ClassVar[ForeignRelation["Salutation"]] = ForeignRelation("Salutation", "salutation_id")


class CustomerAddress(CustomerAddressBase["CustomerAddressEndpoint"], CustomerAddressRelations):
    pass


class CustomerAddressEndpoint(EndpointBase[CustomerAddress]):
    name = "customer_address"
    path = "/customer-address"
    model_class = CustomerAddress


registry.register_admin(CustomerAddressEndpoint)
