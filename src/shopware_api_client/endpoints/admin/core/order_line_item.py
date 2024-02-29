from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField, Price
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import (
        Media,
        Order,
        OrderDeliveryPosition,
        OrderLineItemDownload,
        OrderTransactionCaptureRefundPosition,
        Product,
        Promotion,
    )


class OrderLineItemBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_line_item"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    order_id: IdField = Field(..., serialization_alias="orderId", validation_alias=AliasChoices("order_id", "orderId"))
    order_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderVersionId",
        validation_alias=AliasChoices("order_version_id", "orderVersionId"),
    )
    product_id: IdField | None = Field(
        default=None, serialization_alias="productId", validation_alias=AliasChoices("product_id", "productId")
    )
    product_version_id: IdField | None = Field(
        default=None,
        serialization_alias="productVersionId",
        validation_alias=AliasChoices("product_version_id", "productVersionId"),
    )
    promotion_id: IdField | None = Field(
        default=None,
        serialization_alias="promotionId",
        validation_alias=AliasChoices("promotion_id", "promotionId"),
        exclude=True,
    )
    parent_id: IdField | None = Field(
        default=None, serialization_alias="parentId", validation_alias=AliasChoices("parent_id", "parentId")
    )
    parent_version_id: IdField | None = Field(
        default=None,
        serialization_alias="parentVersionId",
        validation_alias=AliasChoices("parent_version_id", "parentVersionId"),
    )
    cover_id: IdField | None = Field(
        default=None, serialization_alias="coverId", validation_alias=AliasChoices("cover_id", "coverId")
    )
    identifier: str
    referenced_id: str | None = Field(
        default=None, serialization_alias="referencedId", validation_alias=AliasChoices("referenced_id", "referencedId")
    )
    quantity: int
    label: str
    payload: dict[str, Any] | None = None
    good: bool | None = None
    removable: bool | None = None
    stackable: bool | None = None
    position: int
    states: list[str]
    price: Price
    price_definition: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="priceDefinition",
        validation_alias=AliasChoices("price_definition", "priceDefinition"),
    )
    unit_price: float | None = Field(
        default=None, serialization_alias="unitPrice", validation_alias=AliasChoices("unit_price", "unitPrice")
    )
    total_price: float | None = Field(
        default=None, serialization_alias="totalPrice", validation_alias=AliasChoices("total_price", "totalPrice")
    )
    description: str | None = None
    type: str | None = None
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


class OrderLineItemRelations:
    cover: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "cover_id")
    order: ClassVar[ForeignRelation["Order"]] = ForeignRelation("Order", "order_id")
    product: ClassVar[ForeignRelation["Product"]] = ForeignRelation("Product", "product_id")
    promotion: ClassVar[ForeignRelation["Promotion"]] = ForeignRelation("Promotion", "promotion_id")
    order_delivery_positions: ClassVar[ManyRelation["OrderDeliveryPosition"]] = ManyRelation(
        "OrderDeliveryPosition", "orderDeliveryPositions"
    )
    order_transaction_capture_refund_positions: ClassVar[
        ManyRelation["OrderTransactionCaptureRefundPosition"]
    ] = ManyRelation("OrderTransactionCaptureRefundPosition", "orderTransactionCaptureRefundPositions")
    downloads: ClassVar[ManyRelation["OrderLineItemDownload"]] = ManyRelation("OrderLineItemDownload", "downloads")
    parent: ClassVar[ForeignRelation["OrderLineItem"]] = ForeignRelation("OrderLineItem", "parent_id")
    children: ClassVar[ManyRelation["OrderLineItem"]] = ManyRelation("OrderLineItem", "children")


class OrderLineItem(OrderLineItemBase["OrderLineItemEndpoint"], OrderLineItemRelations):
    pass


class OrderLineItemEndpoint(EndpointBase[OrderLineItem]):
    name = "order_line_item"
    path = "/order-line-item"
    model_class = OrderLineItem


registry.register_admin(OrderLineItemEndpoint)
