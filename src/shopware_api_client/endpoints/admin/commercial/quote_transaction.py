from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.quote_transaction import QuoteTransactionBase


class QuoteTransaction(QuoteTransactionBase, AdminModel["QuoteTransactionEndpoint"]):
    quote: ForeignRelation["Quote"] = Field(default=...)
    payment_method: ForeignRelation["PaymentMethod"] = Field(default=...)


class QuoteTransactionEndpoint(AdminEndpoint[QuoteTransaction]):
    name = "quote_transaction"
    path = "/quote-transaction"
    model_class = QuoteTransaction


from ..core.payment_method import PaymentMethod  # noqa: E402
from .quote import Quote  # noqa: E402
