from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class CustomerWishlistBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "customer_wishlist"

    customer_id: IdField
    sales_channel_id: IdField
