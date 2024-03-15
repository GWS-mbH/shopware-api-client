from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class OrderAddressBase(ApiModelBase[EndpointClass]):
    _identifier: str = "order_address"

    version_id: IdField | None = None
    country_id: IdField
    country_state_id: IdField | None = None
    order_id: IdField
    order_version_id: IdField | None = None
    salutation_id: IdField | None = None
    first_name: str
    last_name: str
    street: str
    zipcode: str | None = None
    city: str
    company: str | None = None
    department: str | None = None
    title: str | None = None
    vat_id: str | None = None
    phone_number: str | None = None
    additional_address_line1: str | None = None
    additional_address_line2: str | None = None
    custom_fields: dict[str, Any] | None = None


class OrderAddressRelations:
    country: ForeignRelation["Country"]
    country_state: ForeignRelation["CountryState"]
    order: ForeignRelation["Order"]
    order_deliveries: ManyRelation["OrderDelivery"]
    salutation: ManyRelation["Salutation"]


class OrderAddress(OrderAddressBase["OrderAddressEndpoint"], OrderAddressRelations):
    pass


class OrderAddressEndpoint(EndpointBase[OrderAddress]):
    name = "order_address"
    path = "/order-address"
    model_class = OrderAddress


from .country import Country  # noqa: E402
from .country_state import CountryState  # noqa: E402
from .order import Order  # noqa: E402
from .order_delivery import OrderDelivery  # noqa: E402
from .salutation import Salutation  # noqa: E402
