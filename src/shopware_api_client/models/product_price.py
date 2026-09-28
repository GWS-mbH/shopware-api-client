
from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo
from shopware_api_client.structs.price import Price


class ProductPriceBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_price"

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    rule_id: Annotated[IdField, RefersTo("rule")]
    price: list[Price]
    quantity_start: int
    quantity_end: int | None = None
