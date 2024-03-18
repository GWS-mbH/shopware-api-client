from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class OrderCustomerBase(ApiModelBase[EndpointClass]):
    _identifier: str = "language"

    version_id: IdField | None = None
    customer_id: IdField | None = None
    order_id: IdField
    order_version_id: IdField | None = None
    email: str
    salutation_id: IdField | None = None
    first_name: str
    last_name: str
    company: str | None = None
    title: str | None = None
    vat_ids: list[str] | None = None
    customer_number: str | None = None
    custom_fields: dict[str, Any] | None = None
    remote_address: str | None = None


class OrderCustomerRelations:
    order: ForeignRelation["Order"]
    customer: ForeignRelation["Customer"]
    salutation: ForeignRelation["Salutation"]


class OrderCustomer(OrderCustomerBase["OrderCustomerEndpoint"], OrderCustomerRelations):
    pass


class OrderCustomerEndpoint(EndpointBase[OrderCustomer]):
    name = "order_customer"
    path = "/order-customer"
    model_class = OrderCustomer


from .customer import Customer  # noqa: E402
from .order import Order  # noqa: E402
from .salutation import Salutation  # noqa: E402
