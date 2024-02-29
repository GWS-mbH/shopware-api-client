from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Product, Rule


class ProductPriceBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_price"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    rule_id: IdField = Field(..., serialization_alias="ruleId", validation_alias=AliasChoices("rule_id", "ruleId"))
    price: dict[str, Any]
    quantity_start: int = Field(
        ..., serialization_alias="quantityStart", validation_alias=AliasChoices("quantity_start", "quantityStart")
    )
    quantity_end: int | None = Field(
        default=None, serialization_alias="quantityEnd", validation_alias=AliasChoices("quantity_end", "quantityEnd")
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


class ProductPriceRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    rule: ClassVar[ForeignRelation["Rule"]] = ForeignRelation("Rule", "rule_id")


class ProductPrice(ProductPriceBase["ProductPriceEndpoint"], ProductPriceRelations):
    pass


class ProductPriceEndpoint(EndpointBase[ProductPrice]):
    name = "product_price"
    path = "/product-price"
    model_class = ProductPrice


registry.register_admin(ProductPriceEndpoint)
