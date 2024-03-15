from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...relations import ManyRelation


class SalutationBase(ApiModelBase[EndpointClass]):
    _identifier: str = "salutation"

    salutation_key: str
    display_name: str
    letter_name: str
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class SalutationRelations:
    customers: ManyRelation["Customer"]
    customer_addresses: ManyRelation["CustomerAddress"]
    order_customers: ManyRelation["OrderCustomer"]
    order_addresses: ManyRelation["OrderAddress"]

    """
    Todo:
    newsletter_recipients[NewsletterRecipient]
    """


class Salutation(SalutationBase["SalutationEndpoint"], SalutationRelations):
    pass


class SalutationEndpoint(EndpointBase[Salutation]):
    name = "salutation"
    path = "/salutation"
    model_class = Salutation


from .customer import Customer  # noqa: E402
from .customer_address import CustomerAddress  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
from .order_customer import OrderCustomer  # noqa: E402
