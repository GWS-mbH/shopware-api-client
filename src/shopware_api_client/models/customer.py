from pydantic import AwareDatetime, Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class CustomerBase(ApiModelBase, CustomFieldsMixin):
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
    remote_address: str | None = None
    tag_ids: list[IdField] | None = Field(default=None, exclude=True)
    requested_group_id: IdField | None = None
    bound_sales_channel_id: IdField | None = None
    account_type: str
    created_by_id: IdField | None = None
    updated_by_id: IdField | None = None
