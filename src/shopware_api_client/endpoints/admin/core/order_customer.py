from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.order_customer import OrderCustomerBase


class OrderCustomer(OrderCustomerBase, AdminModel["OrderCustomerEndpoint"]):
    order_id: IdField
    order: ForeignRelation["Order"] = Field(default=...)
    customer: ForeignRelation["Customer"] = Field(default=...)
    salutation: ForeignRelation["Salutation"] = Field(default=...)


class OrderCustomerEndpoint(AdminEndpoint[OrderCustomer]):
    name = "order_customer"
    path = "/order-customer"
    model_class = OrderCustomer


from .customer import Customer  # noqa: E402
from .order import Order  # noqa: E402
from .salutation import Salutation  # noqa: E402
