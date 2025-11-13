from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class ProductCrossSellingAssignedProductsBase(ApiModelBase):
    _identifier: str = "product_cross_selling_assigned_products"

    cross_selling_id: IdField
    product_id: IdField
    product_version_id: IdField | None = None
    position: int | None = None
