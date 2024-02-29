from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import Amount, IdField, Price, Rounding
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import (
        Currency,
        Document,
        Language,
        OrderAddress,
        OrderCustomer,
        OrderDelivery,
        OrderLineItem,
        OrderTransaction,
        SalesChannel,
        StateMachineState,
        Tag,
        User,
    )


class OrderBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order"

    version_id: IdField | None = Field(
        default=None, serialization_alias="versionId", validation_alias=AliasChoices("version_id", "versionId")
    )
    auto_increment: int | None = Field(
        default=None,
        serialization_alias="autoIncrement",
        validation_alias=AliasChoices("auto_increment", "autoIncrement"),
        exclude=True,
    )
    order_number: str | None = Field(
        default=None, serialization_alias="orderNumber", validation_alias=AliasChoices("order_number", "orderNumber")
    )
    billing_address_id: IdField = Field(
        ...,
        serialization_alias="billingAddressId",
        validation_alias=AliasChoices("billing_address_id", "billingAddressId"),
    )
    billing_address_version_id: IdField | None = Field(
        default=None,
        serialization_alias="billingAddressVersionId",
        validation_alias=AliasChoices("billing_address_version_id", "billingAddressVersionId"),
    )
    currency_id: IdField = Field(
        ..., serialization_alias="currencyId", validation_alias=AliasChoices("currency_id", "currencyId")
    )
    language_id: IdField = Field(
        ..., serialization_alias="languageId", validation_alias=AliasChoices("language_id", "languageId")
    )
    sales_channel_id: IdField = Field(
        ..., serialization_alias="salesChannelId", validation_alias=AliasChoices("sales_channel_id", "salesChannelId")
    )
    order_date_time: AwareDatetime = Field(
        ..., serialization_alias="orderDateTime", validation_alias=AliasChoices("order_date_time", "orderDateTime")
    )
    order_date: str | None = Field(
        default=None,
        serialization_alias="orderDate",
        validation_alias=AliasChoices("order_date", "orderDate"),
        exclude=True,
    )
    price: Price | None = None
    amount_total: float | None = Field(
        default=None,
        serialization_alias="amountTotal",
        validation_alias=AliasChoices("amount_total", "amountTotal"),
        exclude=True,
    )
    amount_net: float | None = Field(
        default=None,
        serialization_alias="amountNet",
        validation_alias=AliasChoices("amount_net", "amountNet"),
        exclude=True,
    )
    position_price: float | None = Field(
        default=None,
        serialization_alias="positionPrice",
        validation_alias=AliasChoices("position_price", "positionPrice"),
        exclude=True,
    )
    tax_status: str | None = Field(
        default=None,
        serialization_alias="taxStatus",
        validation_alias=AliasChoices("tax_status", "taxStatus"),
        exclude=True,
    )
    shipping_costs: Amount | None = Field(
        default=None,
        serialization_alias="shippingCosts",
        validation_alias=AliasChoices("shipping_costs", "shippingCosts"),
    )
    shipping_total: float | None = Field(
        default=None,
        serialization_alias="shippingTotal",
        validation_alias=AliasChoices("shipping_total", "shippingTotal"),
        exclude=True,
    )
    currency_factor: float = Field(
        ..., serialization_alias="currencyFactor", validation_alias=AliasChoices("currency_factor", "currencyFactor")
    )
    deep_link_code: str | None = Field(
        default=None,
        serialization_alias="deepLinkCode",
        validation_alias=AliasChoices("deep_link_code", "deepLinkCode"),
    )
    affiliate_code: str | None = Field(
        default=None,
        serialization_alias="affiliateCode",
        validation_alias=AliasChoices("affiliate_code", "affiliateCode"),
    )
    campaign_code: str | None = Field(
        default=None, serialization_alias="campaignCode", validation_alias=AliasChoices("campaign_code", "campaignCode")
    )
    customer_comment: str | None = Field(
        default=None,
        serialization_alias="customerComment",
        validation_alias=AliasChoices("customer_comment", "customerComment"),
    )
    source: str | None = None
    state_id: IdField = Field(..., serialization_alias="stateId", validation_alias=AliasChoices("state_id", "stateId"))
    rule_ids: list[str] | None = Field(
        default=None, serialization_alias="ruleIds", validation_alias=AliasChoices("rule_ids", "ruleIds")
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    created_by_id: IdField | None = Field(
        default=None, serialization_alias="createdById", validation_alias=AliasChoices("created_by_id", "createdById")
    )
    updated_by_id: IdField | None = Field(
        default=None, serialization_alias="updatedById", validation_alias=AliasChoices("updated_by_id", "updatedById")
    )
    item_rounding: Rounding = Field(
        ..., serialization_alias="itemRounding", validation_alias=AliasChoices("item_rounding", "itemRounding")
    )
    total_rounding: Rounding = Field(
        ..., serialization_alias="totalRounding", validation_alias=AliasChoices("total_rounding", "totalRounding")
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


class OrderRelations:
    state: ClassVar[ForeignRelation["StateMachineState"]] = ForeignRelation("StateMachineState", "state_id")
    order_customer: ClassVar[ManyRelation["OrderCustomer"]] = ManyRelation("OrderCustomer", "orderCustomer")
    currency: ClassVar[ForeignRelation["Currency"]] = ForeignRelation("Currency", "currency_id")
    language: ClassVar[ForeignRelation["Language"]] = ForeignRelation("Language", "language_id")
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")
    addresses: ClassVar[ManyRelation["OrderAddress"]] = ManyRelation("OrderAddress", "addresses")
    billing_address: ClassVar[ForeignRelation["OrderAddress"]] = ForeignRelation("OrderAddress", "billing_address_id")
    deliveries: ClassVar[ManyRelation["OrderDelivery"]] = ManyRelation("OrderDelivery", "deliveries")
    line_items: ClassVar[ManyRelation["OrderLineItem"]] = ManyRelation("OrderLineItem", "lineItems")
    transactions: ClassVar[ManyRelation["OrderTransaction"]] = ManyRelation("OrderTransaction", "transactions")
    documents: ClassVar[ManyRelation["Document"]] = ManyRelation("Document", "documents")
    tags: ClassVar[ManyRelation["Tag"]] = ManyRelation("Tag", "tags")
    created_by: ClassVar[ForeignRelation["User"]] = ForeignRelation("User", "created_by_id")
    updated_by: ClassVar[ForeignRelation["User"]] = ForeignRelation("User", "updated_by_id")


class Order(OrderBase["OrderEndpoint"], OrderRelations):
    pass


class OrderEndpoint(EndpointBase[Order]):
    name = "order"
    path = "/order"
    model_class = Order


registry.register_admin(OrderEndpoint)
