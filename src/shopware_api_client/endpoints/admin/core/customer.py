from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import AliasChoices, AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ....client import registry
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

if TYPE_CHECKING:
    from ...admin import (
        CustomerAddress,
        CustomerGroup,
        CustomerRecovery,
        CustomerWishlist,
        Language,
        OrderCustomer,
        PaymentMethod,
        ProductReview,
        Promotion,
        SalesChannel,
        Salutation,
        Tag,
        User,
    )


class CustomerBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer"

    group_id: IdField = Field(..., serialization_alias="groupId", validation_alias=AliasChoices("group_id", "groupId"))
    default_payment_method_id: IdField = Field(
        ...,
        serialization_alias="defaultPaymentMethodId",
        validation_alias=AliasChoices("default_payment_method_id", "defaultPaymentMethodId"),
    )
    sales_channel_id: IdField = Field(
        ..., serialization_alias="salesChannelId", validation_alias=AliasChoices("sales_channel_id", "salesChannelId")
    )
    language_id: IdField = Field(
        ..., serialization_alias="languageId", validation_alias=AliasChoices("language_id", "languageId")
    )
    last_payment_method_id: IdField | None = Field(
        default=None,
        serialization_alias="lastPaymentMethodId",
        validation_alias=AliasChoices("last_payment_method_id", "lastPaymentMethodId"),
    )
    default_billing_address_id: IdField = Field(
        ...,
        serialization_alias="defaultBillingAddressId",
        validation_alias=AliasChoices("default_billing_address_id", "defaultBillingAddressId"),
    )
    default_shipping_address_id: IdField = Field(
        ...,
        serialization_alias="defaultShippingAddressId",
        validation_alias=AliasChoices("default_shipping_address_id", "defaultShippingAddressId"),
    )
    auto_increment: int | None = Field(
        default=None,
        serialization_alias="autoIncrement",
        validation_alias=AliasChoices("auto_increment", "autoIncrement"),
        exclude=True,
    )
    customer_number: str = Field(
        ..., serialization_alias="customerNumber", validation_alias=AliasChoices("customer_number", "customerNumber")
    )
    salutation_id: IdField | None = Field(
        default=None, serialization_alias="salutationId", validation_alias=AliasChoices("salutation_id", "salutationId")
    )
    first_name: str = Field(
        ..., serialization_alias="firstName", validation_alias=AliasChoices("first_name", "firstName")
    )
    last_name: str = Field(..., serialization_alias="lastName", validation_alias=AliasChoices("last_name", "lastName"))
    company: str | None = None
    email: str
    title: str | None = None
    vat_ids: list[str] | None = Field(
        default=None, serialization_alias="vatIds", validation_alias=AliasChoices("vat_ids", "vatIds")
    )
    affiliate_code: str | None = Field(
        default=None,
        serialization_alias="affiliateCode",
        validation_alias=AliasChoices("affiliate_code", "affiliateCode"),
    )
    campaign_code: str | None = Field(
        default=None, serialization_alias="campaignCode", validation_alias=AliasChoices("campaign_code", "campaignCode")
    )
    active: bool | None = None
    double_opt_in_registration: bool | None = Field(
        default=None,
        serialization_alias="doubleOptInRegistration",
        validation_alias=AliasChoices("double_opt_in_registration", "doubleOptInRegistration"),
    )
    double_opt_in_email_sent_date: AwareDatetime | None = Field(
        default=None, serialization_alias="doubleOptInEmailSentDate"
    )
    double_opt_in_confirm_date: AwareDatetime | None = Field(
        default=None,
        serialization_alias="doubleOptInConfirmDate",
        validation_alias=AliasChoices("double_opt_in_confirm_date", "doubleOptInConfirmDate"),
    )
    hash: str | None = None
    guest: bool | None = None
    first_login: AwareDatetime | None = Field(
        default=None, serialization_alias="firstLogin", validation_alias=AliasChoices("first_login", "firstLogin")
    )
    last_login: AwareDatetime | None = Field(
        default=None, serialization_alias="lastLogin", validation_alias=AliasChoices("last_login", "lastLogin")
    )
    birthday: str | None = None
    last_order_date: AwareDatetime | None = Field(
        default=None,
        serialization_alias="lastOrderDate",
        validation_alias=AliasChoices("last_order_date", "lastOrderDate"),
        exclude=True,
    )
    order_count: int | None = Field(
        default=None,
        serialization_alias="orderCount",
        validation_alias=AliasChoices("order_count", "orderCount"),
        exclude=True,
    )
    order_total_amount: float | None = Field(
        default=None,
        serialization_alias="orderTotalAmount",
        validation_alias=AliasChoices("order_total_amount", "orderTotalAmount"),
        exclude=True,
    )
    review_count: int | None = Field(
        default=None,
        serialization_alias="reviewCount",
        validation_alias=AliasChoices("review_count", "reviewCount"),
        exclude=True,
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None, serialization_alias="customFields", validation_alias=AliasChoices("custom_fields", "customFields")
    )
    remote_address: str | None = Field(
        default=None,
        serialization_alias="remoteAddress",
        validation_alias=AliasChoices("remote_address", "remoteAddress"),
    )
    tag_ids: list[IdField] | None = Field(
        default=None, serialization_alias="tagIds", validation_alias=AliasChoices("tag_ids", "tagIds"), exclude=True
    )
    requested_group_id: IdField | None = Field(
        default=None,
        serialization_alias="requestedGroupId",
        validation_alias=AliasChoices("requested_group_id", "requestedGroupId"),
    )
    bound_sales_channel_id: IdField | None = Field(
        default=None,
        serialization_alias="boundSalesChannelId",
        validation_alias=AliasChoices("bound_sales_channel_id", "boundSalesChannelId"),
    )
    account_type: str = Field(
        ..., serialization_alias="accountType", validation_alias=AliasChoices("account_type", "accountType")
    )
    created_by_id: IdField | None = Field(
        default=None, serialization_alias="createdById", validation_alias=AliasChoices("created_by_id", "createdById")
    )
    updated_by_id: IdField | None = Field(
        default=None, serialization_alias="updatedById", validation_alias=AliasChoices("updated_by_id", "updatedById")
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


class CustomerBaseRelations:
    group: ClassVar[ForeignRelation["CustomerGroup"]] = ForeignRelation("CustomerGroup", "group_id")
    default_payment_method: ClassVar[ForeignRelation["PaymentMethod"]] = ForeignRelation(
        "PaymentMethod", "default_payment_method_id"
    )
    sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation("SalesChannel", "sales_channel_id")
    language: ClassVar[ForeignRelation["Language"]] = ForeignRelation("Language", "language_id")
    last_payment_method: ClassVar[ForeignRelation["PaymentMethod"]] = ForeignRelation(
        "PaymentMethod", "last_payment_method_id"
    )
    default_billing_address: ClassVar[ForeignRelation["CustomerAddress"]] = ForeignRelation(
        "CustomerAddress", "default_billing_address_id"
    )
    default_shipping_address: ClassVar[ForeignRelation["CustomerAddress"]] = ForeignRelation(
        "CustomerAddress", "default_shipping_address_id"
    )
    salutation: ClassVar[ForeignRelation["Salutation"]] = ForeignRelation("Salutation", "salutation_id")
    addresses: ClassVar[ManyRelation["CustomerAddress"]] = ManyRelation("CustomerAddress", "addresses")
    order_customers: ClassVar[ManyRelation["OrderCustomer"]] = ManyRelation("OrderCustomer", "orderCustomers")
    tags: ClassVar[ManyRelation["Tag"]] = ManyRelation("Tag", "tags")
    promotions: ClassVar[ManyRelation["Promotion"]] = ManyRelation("Promotion", "promotions")
    product_reviews: ClassVar[ManyRelation["ProductReview"]] = ManyRelation("ProductReview", "productReviews")
    recovery_customer: ClassVar[ManyRelation["CustomerRecovery"]] = ManyRelation("CustomerRecovery", "recoveryCustomer")
    requested_group: ClassVar[ForeignRelation["CustomerGroup"]] = ForeignRelation("CustomerGroup", "requested_group_id")
    bound_sales_channel: ClassVar[ForeignRelation["SalesChannel"]] = ForeignRelation(
        "SalesChannel", "bound_sales_channel_id"
    )
    wishlists: ClassVar[ManyRelation["CustomerWishlist"]] = ManyRelation("CustomerWishlist", "wishlists")
    created_by: ClassVar[ForeignRelation["User"]] = ForeignRelation("User", "created_by_id")
    updated_by: ClassVar[ForeignRelation["User"]] = ForeignRelation("User", "updated_by_id")


class Customer(CustomerBase["CustomerEndpoint"], CustomerBaseRelations):
    pass


class CustomerEndpoint(EndpointBase[Customer]):
    name = "customer"
    path = "/customer"
    model_class = Customer


registry.register_admin(CustomerEndpoint)
