from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import OrderLineItem, OrderTransactionCaptureRefund


class OrderTransactionCaptureRefundPositionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_transaction_capture_refund_position"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    refund_id: IdField = Field(
        ..., serialization_alias="refundId", validation_alias=AliasChoices("refund_id", "refundId")
    )
    refund_version_id: IdField | None = Field(
        default=None,
        serialization_alias="refundVersionId",
        validation_alias=AliasChoices("refund_version_id", "refundVersionId"),
    )
    order_line_item_id: IdField = Field(
        ...,
        serialization_alias="orderLineItemId",
        validation_alias=AliasChoices("order_line_item_id", "orderLineItemId"),
    )
    order_line_item_version_id: IdField | None = Field(
        default=None,
        serialization_alias="orderLineItemVersionId",
        validation_alias=AliasChoices("order_line_item_version_id", "orderLineItemVersionId"),
    )
    external_reference: str | None = Field(
        default=None,
        serialization_alias="externalReference",
        validation_alias=AliasChoices("external_reference", "externalReference"),
    )
    reason: str | None = None
    quantity: int | None = None
    amount: Amount
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


class OrderTransactionCaptureRefundPositionRelations:
    order_line_item: ClassVar[ForeignRelation["OrderLineItem"]] = ForeignRelation("OrderLineItem", "order_line_item_id")
    refund: ClassVar[ForeignRelation["OrderTransactionCaptureRefund"]] = ForeignRelation(
        "OrderTransactionCaptureRefund", "refund_id"
    )


class OrderTransactionCaptureRefundPosition(
    OrderTransactionCaptureRefundPositionBase["OrderTransactionCaptureRefundPositionEndpoint"],
    OrderTransactionCaptureRefundPositionRelations,
):
    pass


class OrderTransactionCaptureRefundPositionEndpoint(EndpointBase[OrderTransactionCaptureRefundPosition]):
    name = "order_transaction_capture_refund_position"
    path = "/order-transaction-capture-refund-position"
    model_class = OrderTransactionCaptureRefundPosition


registry.register_admin(OrderTransactionCaptureRefundPositionEndpoint)
