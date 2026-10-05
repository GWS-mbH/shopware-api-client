from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductCrossSellingAssignedProductsBase(ApiModelBase):
    _identifier: str = "product_cross_selling_assigned_products"

    cross_selling_id: Annotated[IdField, RefersTo("product_cross_selling")]
    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    position: int | None = None
