from typing import Any

from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.exceptions import SWAPIMethodNotAvailable
from shopware_api_client.models.product_category import ProductCategoryBase


class ProductCategory(ProductCategoryBase, AdminModel["ProductCategoryEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    category: ForeignRelation["Category"] = Field(default=...)

    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        raise SWAPIMethodNotAvailable("Mapping entities have no id. Use `bulk_delete()` instead.")


class ProductCategoryEndpoint(AdminEndpoint[ProductCategory]):
    name = "product_category"
    path = "/product-category"
    model_class = ProductCategory

    async def get(self, *args: Any, **kwargs: Any) -> Any:
        raise SWAPIMethodNotAvailable("Mapping entities have no id. Use `filter()` instead.")

    async def update(self, *args: Any, **kwargs: Any) -> Any:
        raise SWAPIMethodNotAvailable("Mapping entities have no id. Use `bulk_upsert()` instead.")

    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        raise SWAPIMethodNotAvailable("Mapping entities have no id. Use `bulk_delete()` instead.")


from .category import Category  # noqa: E402
from .product import Product  # noqa: E402
