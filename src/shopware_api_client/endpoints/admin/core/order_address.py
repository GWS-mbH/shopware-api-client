from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.base_fields import IdField
from shopware_api_client.endpoints.relations import ForeignRelation, ManyRelation
from shopware_api_client.models.order_address import OrderAddress as OrderAddressBase


class OrderAddress(OrderAddressBase, AdminModel["OrderAddressEndpoint"]):
    order_id: IdField
    country: ForeignRelation["Country"]
    country_state: ForeignRelation["CountryState"]
    order: ForeignRelation["Order"]
    order_deliveries: ManyRelation["OrderDelivery"]
    salutation: ManyRelation["Salutation"]


class OrderAddressEndpoint(AdminEndpoint[OrderAddress]):
    name = "order_address"
    path = "/order-address"
    model_class = OrderAddress


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .order import Order  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .salutation import Salutation  # noqa: E402
