from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.payment_method import PaymentMethodBase


class PaymentMethod(PaymentMethodBase, AdminModel["PaymentMethodEndpoint"]):
    media: ForeignRelation["Media"] = Field(default=...)
    availability_rule: ForeignRelation["Rule"] = Field(default=...)
    sales_channel_default_assignments: ManyRelation["SalesChannel"] = Field(default=...)
    customers: ManyRelation["Customer"] = Field(default=...)
    order_transactions: ManyRelation["OrderTransaction"] = Field(default=...)
    sales_channels: ManyRelation["SalesChannel"] = Field(default=...)

    """
    Todo:
    plugin[Plugin], orderTransactions, app_payment_method[AppPaymentMethod]
    """


class PaymentMethodEndpoint(AdminEndpoint[PaymentMethod]):
    name = "payment_method"
    path = "/payment-method"
    model_class = PaymentMethod


from .customer import Customer  # noqa: E402
from .media import Media  # noqa: E402
from .order_transaction import OrderTransaction  # noqa: E402
from .rule import Rule  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
