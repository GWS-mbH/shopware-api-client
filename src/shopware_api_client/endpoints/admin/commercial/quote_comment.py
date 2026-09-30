from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.quote_comment import QuoteCommentBase


class QuoteComment(QuoteCommentBase, AdminModel["QuoteCommentEndpoint"]):
    quote: ForeignRelation["Quote"] = Field(default=...)
    state: ForeignRelation["StateMachineState"] = Field(default=...)
    customer: ForeignRelation["Customer"] = Field(default=...)
    employee: ForeignRelation["B2bEmployee"] = Field(default=...)
    created_by: ForeignRelation["User"] = Field(default=...)


class QuoteCommentEndpoint(AdminEndpoint[QuoteComment]):
    name = "quote_comment"
    path = "/quote-comment"
    model_class = QuoteComment


from ..core.customer import Customer  # noqa: E402
from ..core.state_machine_state import StateMachineState  # noqa: E402
from ..core.user import User  # noqa: E402
from .b2b_employee import B2bEmployee  # noqa: E402
from .quote import Quote  # noqa: E402
