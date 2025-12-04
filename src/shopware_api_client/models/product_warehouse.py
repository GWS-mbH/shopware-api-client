from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class ProductWarehouseBase(ApiModelBase):
    _identifier = "product_warehouse"

    stock: int
    product_id: IdField
    warehouse_id: IdField
