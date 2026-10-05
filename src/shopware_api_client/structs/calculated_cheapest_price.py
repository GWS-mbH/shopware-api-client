from typing import Annotated

from shopware_api_client.endpoints.base_fields import IdField, RefersTo

from .calculated_price import CalculatedPrice


class CalculatedCheapestPrice(CalculatedPrice):
    has_range: bool
    variant_id: Annotated[IdField | None, RefersTo("product")] = None
