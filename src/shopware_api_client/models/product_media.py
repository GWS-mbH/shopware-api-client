from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductMediaBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_media"

    product_id: Annotated[IdField, RefersTo("product")]
    product_version_id: IdField | None = None
    media_id: Annotated[IdField, RefersTo("media")]
    position: int | None = None
