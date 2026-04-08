from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.order_address import OrderAddressBase


class OrderAddress(OrderAddressBase, AdminModel["OrderAddressEndpoint"]):
    order_id: IdField
    country: ForeignRelation["Country"] = Field(default=...)
    country_state: ForeignRelation["CountryState"] = Field(default=...)
    order: ForeignRelation["Order"] = Field(default=...)
    order_deliveries: ManyRelation["OrderDelivery"] = Field(default=...)
    salutation: ManyRelation["Salutation"] = Field(default=...)


class OrderAddressEndpoint(AdminEndpoint[OrderAddress]):
    name = "order_address"
    path = "/order-address"
    model_class = OrderAddress


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .order import Order  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .salutation import Salutation  # noqa: E402
