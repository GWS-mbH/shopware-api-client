from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Customer, SalesChannel


class CustomerGroupBase(ApiModelBase[EndpointClass]):
    _identifier = "customer_group"

    name: str
    display_gross: bool | None = Field(
        default=None, serialization_alias="displayGross", validation_alias=AliasChoices("display_gross", "displayGross")
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    registration_active: bool | None = Field(
        default=None,
        serialization_alias="registrationActive",
        validation_alias=AliasChoices("registration_active", "registrationActive"),
    )
    registration_title: str | None = Field(
        default=None,
        serialization_alias="registrationTitle",
        validation_alias=AliasChoices("registration_title", "registrationTitle"),
    )
    registration_introduction: str | None = Field(
        default=None,
        serialization_alias="registrationIntroduction",
        validation_alias=AliasChoices("registration_introduction", "registrationIntroduction"),
    )
    registration_only_company_registration: bool | None = Field(
        default=None, serialization_alias="registrationOnlyCompanyRegistration"
    )
    registration_seo_meta_description: str | None = Field(
        default=None, serialization_alias="registrationSeoMetaDescription"
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


class CustomerGroupRelations:
    customers: ClassVar[ManyRelation["Customer"]] = ManyRelation("Customer", "customers")
    sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation("SalesChannel", "salesChannels")
    registration_sales_channels: ClassVar[ManyRelation["SalesChannel"]] = ManyRelation(
        "SalesChannel", "registrationSalesChannels"
    )


class CustomerGroup(CustomerGroupBase["CustomerGroupEndpoint"], CustomerGroupRelations):
    pass


class CustomerGroupEndpoint(EndpointBase[CustomerGroup]):
    name = "customer_group"
    path = "/customer-group"
    model_class = CustomerGroup


registry.register_admin(CustomerGroupEndpoint)
