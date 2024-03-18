from typing import Any

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation, ManyRelation


class CountryStateBase(ApiModelBase[EndpointClass]):
    _identifier: str = "country_state"

    country_id: IdField
    short_code: str
    name: str
    position: int | None = None
    active: bool | None = None
    custom_fields: dict[str, Any] | None = None
    translated: dict[str, Any] | None = None


class CountryStateRelations:
    country: ForeignRelation["Country"]
    customer_addresses: ManyRelation["CustomerAddress"]
    order_addresses: ManyRelation["OrderAddress"]


class CountryState(CountryStateBase["CountryStateEndpoint"], CountryStateRelations):
    pass


class CountryStateEndpoint(EndpointBase[CountryState]):
    name = "country_state"
    path = "/country_state"
    model_class = CountryState


from .country import Country  # noqa: E402
from .customer_address import CustomerAddress  # noqa: E402
from .order_address import OrderAddress  # noqa: E402
