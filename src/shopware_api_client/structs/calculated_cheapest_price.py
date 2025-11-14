from .calculated_price import CalculatedPrice


class CalculatedCheapestPrice(CalculatedPrice):
    has_range: bool
    variant_id: str | None = None
