from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation

if TYPE_CHECKING:
    from ...admin import Media, OrderLineItem


class OrderLineItemDownloadBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_line_item_download"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
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
    media_id: IdField = Field(..., serialization_alias="mediaId", validation_alias=AliasChoices("media_id", "mediaId"))
    position: int
    access_granted: bool = Field(
        ..., serialization_alias="accessGranted", validation_alias=AliasChoices("access_granted", "accessGranted")
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


class OrderLineItemDownloadRelations:
    order_line_item: ClassVar[ForeignRelation["OrderLineItem"]] = ForeignRelation("OrderLineItem", "order_line_item_id")
    media: ClassVar[ForeignRelation["Media"]] = ForeignRelation("Media", "media_id")


class OrderLineItemDownload(OrderLineItemDownloadBase["OrderLineItemDownloadEndpoint"], OrderLineItemDownloadRelations):
    pass


class OrderLineItemDownloadEndpoint(EndpointBase[OrderLineItemDownload]):
    name = "order_line_item_download"
    path = "/order-line-item-download"
    model_class = OrderLineItemDownload


registry.register_admin(OrderLineItemDownloadEndpoint)
