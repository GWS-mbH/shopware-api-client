from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.payment_method import PaymentMethod as PaymentMethodBase


class PaymentMethod(PaymentMethodBase, AdminModel["PaymentMethodEndpoint"]):
    media: ForeignRelation["Media"]
    availability_rule: ForeignRelation["Rule"]
    sales_channel_default_assignments: ManyRelation["SalesChannel"]
    customers: ManyRelation["Customer"]
    order_transactions: ManyRelation["OrderTransaction"]
    sales_channels: ManyRelation["SalesChannel"]

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
