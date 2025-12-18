from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ManyRelation
from shopware_api_client.models.salutation import SalutationBase


class Salutation(SalutationBase, AdminModel["SalutationEndpoint"]):
    customers: ManyRelation["Customer"] = Field(default=...)
    customer_addresses: ManyRelation["CustomerAddress"] = Field(default=...)
    order_customers: ManyRelation["OrderCustomer"] = Field(default=...)
    order_addresses: ManyRelation["OrderAddress"] = Field(default=...)

    """
    Todo:
    newsletter_recipients[NewsletterRecipient]
    """


class SalutationEndpoint(AdminEndpoint[Salutation]):
    name = "salutation"
    path = "/salutation"
    model_class = Salutation


from .customer import Customer  # noqa: E402
from .customer_address import CustomerAddress  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from .order_customer import OrderCustomer  # noqa: E402
