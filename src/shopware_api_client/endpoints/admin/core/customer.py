from typing import Any

from pydantic import AwareDatetime, Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class CustomerBase(ApiModelBase[EndpointClass]):
    _identifier: str = "customer"

    group_id: IdField
    default_payment_method_id: IdField | None = None
    sales_channel_id: IdField
    language_id: IdField
    last_payment_method_id: IdField | None = None
    default_billing_address_id: IdField
    default_shipping_address_id: IdField
    auto_increment: int | None = Field(default=None, exclude=True)
    customer_number: str
    salutation_id: IdField | None = None
    first_name: str
    last_name: str
    company: str | None = None
    email: str
    title: str | None = None
    vat_ids: list[str] | None = None
    affiliate_code: str | None = None
    campaign_code: str | None = None
    active: bool | None = None
    double_opt_in_registration: bool | None = None
    double_opt_in_email_sent_date: AwareDatetime | None = None
    double_opt_in_confirm_date: AwareDatetime | None = None
    hash: str | None = None
    guest: bool | None = None
    first_login: AwareDatetime | None = None
    last_login: AwareDatetime | None = None
    birthday: str | None = None
    last_order_date: AwareDatetime | None = Field(default=None, exclude=True)
    order_count: int | None = Field(default=None, exclude=True)
    order_total_amount: float | None = Field(default=None, exclude=True)
    review_count: int | None = Field(default=None, exclude=True)
    custom_fields: dict[str, Any] | None = None
    remote_address: str | None = None
    tag_ids: list[IdField] | None = Field(default=None, exclude=True)
    requested_group_id: IdField | None = None
    bound_sales_channel_id: IdField | None = None
    account_type: str
    created_by_id: IdField | None = None
    updated_by_id: IdField | None = None


class CustomerBaseRelations:
    group: ForeignRelation["CustomerGroup"]
    default_payment_method: ForeignRelation["PaymentMethod"]
    sales_channel: ForeignRelation["SalesChannel"]
    language: ForeignRelation["Language"]
    last_payment_method: ForeignRelation["PaymentMethod"]
    default_billing_address: ForeignRelation["CustomerAddress"]
    default_shipping_address: ForeignRelation["CustomerAddress"]
    salutation: ForeignRelation["Salutation"]
    addresses: ManyRelation["CustomerAddress"]
    order_customers: ManyRelation["OrderCustomer"]
    tags: ManyRelation["Tag"]
    promotions: ManyRelation["Promotion"]
    product_reviews: ManyRelation["ProductReview"]
    recovery_customer: ManyRelation["CustomerRecovery"]
    requested_group: ForeignRelation["CustomerGroup"]
    bound_sales_channel: ForeignRelation["SalesChannel"]
    wishlists: ManyRelation["CustomerWishlist"]
    created_by: ForeignRelation["User"]
    updated_by: ForeignRelation["User"]


class Customer(CustomerBase["CustomerEndpoint"], CustomerBaseRelations):
    pass


class CustomerEndpoint(EndpointBase[Customer]):
    name = "customer"
    path = "/customer"
    model_class = Customer


from .customer_address import CustomerAddress  # noqa: E402
from .customer_group import CustomerGroup  # noqa: E402
from .customer_recovery import CustomerRecovery  # noqa: E402
from .customer_wishlist import CustomerWishlist  # noqa: E402
from .language import Language  # noqa: E402
from .order_customer import OrderCustomer  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .product_review import ProductReview  # noqa: E402
from .promotion import Promotion  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .salutation import Salutation  # noqa: E402
from .tag import Tag  # noqa: E402
from .user import User  # noqa: E402
