from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class MainCategoryBase(ApiModelBase[EndpointClass]):
    _identifier: str = "main_category"

    product_id: IdField
    product_version_id: IdField | None = None
    category_id: IdField
    category_version_id: IdField | None = None
    sales_channel_id: IdField


class MainCategoryRelations:
    product: ForeignRelation["Product"]
    category: ForeignRelation["Category"]
    sales_channel: ForeignRelation["SalesChannel"]


class MainCategory(MainCategoryBase["MainCategoryEndpoint"], MainCategoryRelations):
    pass


class MainCategoryEndpoint(EndpointBase[MainCategory]):
    name = "main_category"
    path = "/main-category"
    model_class = MainCategory


from .category import Category  # noqa: E402
from .product import Product  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
