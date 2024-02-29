from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Product, Rule, ShippingMethod


class TaxBase(ApiModelBase[EndpointClass]):
    _identifier: str = "tax"

    tax_rate: float = Field(..., serialization_alias="taxRate", validation_alias=AliasChoices("tax_rate", "taxRate"))
    name: str
    position: int = Field(..., description="Added since version: 6.4.0.0.")
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


class TaxRelations:
    products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "products")
    rules: ClassVar[ManyRelation["Rule"]] = ManyRelation("Rule", "rules")
    shipping_methods: ClassVar[ManyRelation["ShippingMethod"]] = ManyRelation("ShippingMethod", "shippingMethods")


class Tax(TaxBase["TaxEndpoint"], TaxRelations):
    pass


class TaxEndpoint(EndpointBase[Tax]):
    name = "tax"
    path = "/tax"
    model_class = Tax


registry.register_admin(TaxEndpoint)
