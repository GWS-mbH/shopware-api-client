from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import Amount, IdField
from ...relations import ForeignRelation, ManyRelation


class OrderTransactionBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_transaction"

    version_id: IdField | None = None
    order_id: IdField
    order_version_id: IdField | None = None
    payment_method_id: IdField
    amount: Amount
    state_id: IdField = Field(..., exclude=True)
    custom_fields: dict[str, Any] | None = None


class OrderTransactionRelations:
    state: ForeignRelation["StateMachineState"]
    order: ForeignRelation["Order"]
    payment_method: ForeignRelation["PaymentMethod"]
    captures: ManyRelation["OrderTransactionCapture"]


class OrderTransaction(OrderTransactionBase["OrderTransactionEndpoint"], OrderTransactionRelations):
    pass


class OrderTransactionEndpoint(EndpointBase[OrderTransaction]):
    name = "order_transaction"
    path = "/order-transaction"
    model_class = OrderTransaction


from .order import Order  # noqa: E402
from .order_transaction_capture import OrderTransactionCapture  # noqa: E402
from .payment_method import PaymentMethod  # noqa: E402
from .state_machine_state import StateMachineState  # noqa: E402
