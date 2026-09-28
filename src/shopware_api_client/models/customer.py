from typing import Annotated

from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class CustomerBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "customer"

    group_id: Annotated[IdField, RefersTo("customer_group")]
    default_payment_method_id: Annotated[IdField | None, RefersTo("payment_method")] = None
    sales_channel_id: Annotated[IdField, RefersTo("sales_channel")]
    language_id: Annotated[IdField, RefersTo("language")]
    last_payment_method_id: Annotated[IdField | None, RefersTo("payment_method")] = None
    default_billing_address_id: Annotated[IdField, RefersTo("customer_address")]
    default_shipping_address_id: Annotated[IdField, RefersTo("customer_address")]
    auto_increment: int | None = Field(default=None, exclude=True)
    customer_number: str
    salutation_id: Annotated[IdField | None, RefersTo("salutation")] = None
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
    remote_address: str | None = None
    tag_ids: list[IdField] | None = Field(default=None, exclude=True)
    requested_group_id: Annotated[IdField | None, RefersTo("customer_group")] = None
    bound_sales_channel_id: Annotated[IdField | None, RefersTo("sales_channel")] = None
    account_type: str
    created_by_id: Annotated[IdField | None, RefersTo("user")] = None
    updated_by_id: Annotated[IdField | None, RefersTo("user")] = None
