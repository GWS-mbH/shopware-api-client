from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class ProductManufacturerBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_manufacturer"

    media_id: Annotated[IdField | None, RefersTo("media")] = None
    link: str | None = None
    name: str
    description: str | None = None
