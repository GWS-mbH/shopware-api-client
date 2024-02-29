from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...relations import ManyRelation

if TYPE_CHECKING:
    from ...admin import Product, ShippingMethod


class DeliveryTimeBase(ApiModelBase[EndpointClass]):
    _identifier: str = "delivery_time"

    name: str
    min: int
    max: int
    unit: str
    custom_fields: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="customFields",
        validation_alias=AliasChoices("custom_fields", "customFields"),
        exclude=True,
    )
    created_at: AwareDatetime = Field(
        ..., serialization_alias="createdAt", validation_alias=AliasChoices("created_at", "createdAt"), exclude=True
    )
    updated_at: AwareDatetime | None = Field(
        default=None, serialization_alias="updatedAt", validation_alias=AliasChoices("updated_at", "updatedAt")
    )
    translated: dict[str, Any] | None = None


class DeliveryTimeRelations:
    shipping_methods: ClassVar[ManyRelation["ShippingMethod"]] = ManyRelation("ShippingMethod", "shippingMethods")
    products: ClassVar[ManyRelation["Product"]] = ManyRelation("Product", "products")


class DeliveryTime(DeliveryTimeBase["DeliveryTimeEndpoint"], DeliveryTimeRelations):
    pass


class DeliveryTimeEndpoint(EndpointBase[DeliveryTime]):
    name = "delivery_time"
    path = "/delivery-time"
    model_class = DeliveryTime


registry.register_admin(DeliveryTimeEndpoint)
