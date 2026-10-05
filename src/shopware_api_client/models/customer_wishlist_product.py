from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class CustomerWishlistProductBase(ApiModelBase):
    _identifier: str = "customer_wishlist_product"

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    wishlist_id: Annotated[IdField, RefersTo("customer_wishlist")]
