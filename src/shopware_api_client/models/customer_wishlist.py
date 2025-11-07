from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class CustomerWishlist(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "customer_wishlist"

    customer_id: IdField
    sales_channel_id: IdField
