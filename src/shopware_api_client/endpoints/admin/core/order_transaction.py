from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.order_transaction import OrderTransactionBase


class OrderTransaction(OrderTransactionBase, AdminModel["OrderTransactionEndpoint"]):
    state: ForeignRelation["StateMachineState"] = Field(default=...)
    order: ForeignRelation["Order"] = Field(default=...)
    payment_method: ForeignRelation["PaymentMethod"] = Field(default=...)
    captures: ManyRelation["OrderTransactionCapture"] = Field(default=...)


class OrderTransactionEndpoint(AdminEndpoint[OrderTransaction]):
    name = "order_transaction"
    path = "/order-transaction"
    model_class = OrderTransaction


from .order import Order  # noqa: E402
from .order_transaction_capture import OrderTransactionCapture  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
