from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Customer, Language, Product, SalesChannel


class ProductReviewBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_review"

    product_id: IdField = Field(
        ..., serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    customer_id: IdField | None = Field(
        default=None, serialization_alias="customerId", validation_alias=AliasChoices("customer_id", "customerId")
    )
    sales_channel_id: IdField = Field(
        ..., serialization_alias="salesChannelId", validation_alias=AliasChoices("sales_channel_id", "salesChannelId")
    )
    language_id: IdField = Field(
        ..., serialization_alias="languageId", validation_alias=AliasChoices("language_id", "languageId")
    )
    external_user: str | None = Field(
        default=None, serialization_alias="externalUser", validation_alias=AliasChoices("external_user", "externalUser")
    )
    external_email: str | None = Field(
        default=None,
        serialization_alias="externalEmail",
        validation_alias=AliasChoices("external_email", "externalEmail"),
    )
    title: str
    content: str
    points: float | None = None
    status: bool | None = None
    comment: str | None = None
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


class ProductReviewRelations:
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    customer: ClassVar[ForeignRelation["Customer"]] = ForeignRelation("Customer", "customer_id")
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")
    language: ClassVar[ForeignRelation["Language"]] = ForeignRelation("Language", "language_id")


class ProductReview(ProductReviewBase["ProductReviewEndpoint"], ProductReviewRelations):
    pass


class ProductReviewEndpoint(EndpointBase[ProductReview]):
    name = "product_review"
    path = "/product-review"
    model_class = ProductReview


registry.register_admin(ProductReviewEndpoint)
