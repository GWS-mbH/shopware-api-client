from pydantic import Field

from shopware_api_client.base import AdminEndpoint, AdminModel
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.quote_employee import QuoteEmployeeBase


class QuoteEmployee(QuoteEmployeeBase, AdminModel["QuoteEmployeeEndpoint"]):
    quote: ForeignRelation["Quote"] = Field(default=...)
    employee: ForeignRelation["B2bEmployee"] = Field(default=...)


class QuoteEmployeeEndpoint(AdminEndpoint[QuoteEmployee]):
    name = "quote_employee"
    path = "/quote-employee"
    model_class = QuoteEmployee


from .b2b_employee import B2bEmployee  # noqa: E402
from .quote import Quote  # noqa: E402
