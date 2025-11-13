from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class ProductDownloadBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "product_download"

    product_id: IdField
    product_version_id: IdField | None = None
    media_id: IdField
    position: int | None = None
