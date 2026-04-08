from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.customer_group import CustomerGroupBase


class CustomerGroup(CustomerGroupBase, AdminModel["CustomerGroupEndpoint"]):
    customers: ManyRelation["Customer"] = Field(default=...)
    sales_channels: ManyRelation["SalesChannel"] = Field(default=...)
    registration_sales_channels: ManyRelation["SalesChannel"] = Field(default=...)


class CustomerGroupEndpoint(AdminEndpoint[CustomerGroup]):
    name = "customer_group"
    path = "/customer-group"
    model_class = CustomerGroup


from .customer import Customer  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
