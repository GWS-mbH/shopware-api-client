from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class OrderCustomerBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "order_customer"

    customer_id: IdField | None = None
    order_version_id: IdField | None = None
    email: str
    salutation_id: IdField | None = None
    first_name: str
    last_name: str
    company: str | None = None
    title: str | None = None
    vat_ids: list[str] | None = None
    customer_number: str | None = None
    remote_address: str | None = None
