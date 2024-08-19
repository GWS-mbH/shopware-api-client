from typing import Any

from pydantic import Field

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation

_FILED_DESCRIPTION = "Runtime field, cannot be used as part of the criteria."


class PaymentMethodBase(ApiModelBase[EndpointClass]):
    _identifier: str = "payment_method"

    plugin_id: IdField | None = None
    handler_identifier: str | None = None
    name: str
    distinguishable_name: str | None = Field(default=None, exclude=True)
    description: str | None = None
    position: int | None = None
    active: bool | None = None
    after_order_enabled: bool | None = None
    custom_fields: dict[str, Any] | None = None
    availability_rule_id: IdField | None = None
    media_id: IdField | None = None
    formatted_handler_identifier: str | None = Field(
        None, description=_FILED_DESCRIPTION, exclude=True
    )
    synchronous: bool | None = Field(
        None, description=_FILED_DESCRIPTION, exclude=True
    )
    asynchronous: bool | None = Field(
        None, description=_FILED_DESCRIPTION, exclude=True
    )
    prepared: bool | None = Field(
        None, description=_FILED_DESCRIPTION, exclude=True
    )
    refundable: bool | None = Field(
        None, description=_FILED_DESCRIPTION, exclude=True
    )
    recurring: bool | None = Field(
        None, description=_FILED_DESCRIPTION, exclude=True
    )
    short_name: str | None = Field(None, description=_FILED_DESCRIPTION)
    technical_name: str | None = Field(default=None, exclude=True)
    translated: dict[str, Any] | None = None


class PaymentMethodRelations:
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


class PaymentMethod(PaymentMethodBase["PaymentMethodEndpoint"], PaymentMethodRelations):
    pass


class PaymentMethodEndpoint(EndpointBase[PaymentMethod]):
    name = "payment_method"
    path = "/payment-method"
    model_class = PaymentMethod


from .customer import Customer  # noqa: E402
from .media import Media  # noqa: E402
from .order_transaction import OrderTransaction  # noqa: E402
from .rule import Rule  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
