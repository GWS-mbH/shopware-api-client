from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class CustomerWishlistBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "customer_wishlist"

    customer_id: Annotated[IdField, RefersTo("customer")]
    sales_channel_id: Annotated[IdField, RefersTo("sales_channel")]
