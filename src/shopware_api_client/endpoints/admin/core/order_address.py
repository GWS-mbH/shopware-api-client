from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Country, CountryState, Order, OrderDelivery, Salutation


class OrderAddressBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_address"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    country_id: IdField = Field(
        ..., serialization_alias="countryId", validation_alias=AliasChoices("country_id", "countryId")
    )
    country_state_id: IdField | None = Field(
        default=None,
        serialization_alias="countryStateId",
        validation_alias=AliasChoices("country_state_id", "countryStateId"),
    )
    order_id: IdField = Field(..., serialization_alias="orderId", validation_alias=AliasChoices("order_id", "orderId"))
    order_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderVersionId",
        validation_alias=AliasChoices("order_version_id", "orderVersionId"),
    )
    salutation_id: IdField | None = Field(
        default=None, serialization_alias="salutationId", validation_alias=AliasChoices("salutation_id", "salutationId")
    )
    first_name: str = Field(
        ..., serialization_alias="firstName", validation_alias=AliasChoices("first_name", "firstName")
    )
    last_name: str = Field(..., serialization_alias="lastName", validation_alias=AliasChoices("last_name", "lastName"))
    street: str
    zipcode: str | None = None
    city: str
    company: str | None = None
    department: str | None = None
    title: str | None = None
    vat_id: str | None = Field(
        default=None, serialization_alias="vatId", validation_alias=AliasChoices("vat_id", "vatId")
    )
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


class OrderAddressRelations:
    country: ClassVar[ForeignRelation["Country"]] = ForeignRelation("Country", "country_id")
    country_state: ClassVar[ForeignRelation["CountryState"]] = ForeignRelation("CountryState", "country_state_id")
    order: ClassVar[ForeignRelation["Order"]] = ForeignRelation("Order", "order_id")
    order_deliveries: ClassVar[ManyRelation["OrderDelivery"]] = ManyRelation("OrderDelivery", "orderDeliveries")
    salutation: ClassVar[ManyRelation["Salutation"]] = ManyRelation("Salutation", "salutation_id")


class OrderAddress(OrderAddressBase["OrderAddressEndpoint"], OrderAddressRelations):
    pass


class OrderAddressEndpoint(EndpointBase[OrderAddress]):
    name = "order_address"
    path = "/order-address"
    model_class = OrderAddress


registry.register_admin(OrderAddressEndpoint)
