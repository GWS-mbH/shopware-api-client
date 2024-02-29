from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import Country, CustomerAddress, OrderAddress


class CountryStateBase(ApiModelBase[EndpointClass]):
    _identifier: str = "country_state"

    country_id: IdField = Field(
        ..., serialization_alias="countryId", validation_alias=AliasChoices("country_id", "countryId")
    )
    short_code: str = Field(
        ..., serialization_alias="shortCode", validation_alias=AliasChoices("short_code", "shortCode")
    )
    name: str
    position: int | None = None
    active: bool | None = None
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


class CountryStateRelations:
    country: ClassVar[ForeignRelation["Country"]] = ForeignRelation("Country", "country_id")
    customer_addresses: ClassVar[ManyRelation["CustomerAddress"]] = ManyRelation("CustomerAddress", "customerAddresses")
    order_addresses: ClassVar[ManyRelation["OrderAddress"]] = ManyRelation("OrderAddress", "orderAddresses")


class CountryState(CountryStateBase["CountryStateEndpoint"], CountryStateRelations):
    pass


class CountryStateEndpoint(EndpointBase[CountryState]):
    name = "country_state"
    path = "/country_state"
    model_class = CountryState


registry.register_admin(CountryStateEndpoint)
