from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.main_category import MainCategoryBase


class MainCategory(MainCategoryBase, AdminModel["MainCategoryEndpoint"]):
    product: ForeignRelation["Product"] = Field(default=...)
    category: ForeignRelation["Category"] = Field(default=...)
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)


class MainCategoryEndpoint(AdminEndpoint[MainCategory]):
    name = "main_category"
    path = "/main-category"
    model_class = MainCategory


from .category import Category  # noqa: E402
from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
