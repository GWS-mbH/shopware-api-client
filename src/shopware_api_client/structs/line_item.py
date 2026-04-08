from typing import Any, Literal

from pydantic import Field

from ..fieldsets import FieldSetBase
from .absolute_price_definition import AbsolutePriceDefinition
from .calculated_price import CalculatedPrice
from .delivery_information import DeliveryInformation
from .quantity_information import QuantityInformation
from .quantity_price_definition import QuantityPriceDefinition
from .reference_price_definition import ReferencePriceDefinition


class LineItem(FieldSetBase):
    children: list["LineItem"] | None = None
    cover: "Media | None" = None
    data_context_hash: str | None = None
    data_timestamp: str | None = None
    delivery_information: DeliveryInformation | None = None
    description: str | None = None
    good: bool | None = True
    id: str
    label: str | None = None
    modified: bool | None = False
    modified_by_app: bool | None = False
    payload: dict[str, Any] = Field(default_factory=dict)
    price: CalculatedPrice | None = None
    price_definition: AbsolutePriceDefinition | QuantityPriceDefinition | ReferencePriceDefinition | None = None
    quantity: int | None = 1
    quantity_information: QuantityInformation | None = None
    referenced_id: str | None = None
    removable: bool | None = False
    stackable: bool | None = False
    states: list[Literal["is-physical", "is-download"]] | None = None
    type: Literal[
        "product",
        "credit",
        "custom",
        "promotion",
        "discount",
        "container",
        "quantity",
        "customized-products",
        "customized-products-option",
        "option-values",
    ]
    unique_identifier: str | None = None


from ..endpoints.store.core.media import Media  # noqa: E402
