from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class CustomerWishlistProductBase(ApiModelBase):
    _identifier: str = "customer_wishlist_product"

    product_id: IdField
    product_version_id: IdField | None = None
    wishlist_id: IdField
