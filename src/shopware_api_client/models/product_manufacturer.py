from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class ProductManufacturerBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_manufacturer"

    media_id: IdField | None = None
    link: str | None = None
    name: str
    description: str | None = None
