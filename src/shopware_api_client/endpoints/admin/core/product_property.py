from typing import Any

from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.exceptions import SWAPIMethodNotAvailable
from shopware_api_client.models.product_property import ProductPropertyBase


class ProductProperty(ProductPropertyBase, AdminModel["ProductPropertyEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    option: ForeignRelation["PropertyGroupOption"] = Field(default=...)

    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        raise SWAPIMethodNotAvailable("Mapping entities have no id. Use `bulk_delete()` instead.")


class ProductPropertyEndpoint(AdminEndpoint[ProductProperty]):
    name = "product_property"
    path = "/product-property"
    model_class = ProductProperty

    async def get(self, *args: Any, **kwargs: Any) -> Any:
        raise SWAPIMethodNotAvailable("Mapping entities have no id. Use `filter()` instead.")

    async def update(self, *args: Any, **kwargs: Any) -> Any:
        raise SWAPIMethodNotAvailable("Mapping entities have no id. Use `bulk_upsert()` instead.")

    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        raise SWAPIMethodNotAvailable("Mapping entities have no id. Use `bulk_delete()` instead.")


from .product import Product  # noqa: E402
from .property_group_option import PropertyGroupOption  # noqa: E402
