from pydantic import Field

from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_export import ProductExportBase


class ProductExport(ProductExportBase, AdminModel["ProductExportEndpoint"]):
    product_stream: ForeignRelation["ProductStream"] = Field(default=...)
    storefront_sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    sales_channel: ForeignRelation["SalesChannel"] = Field(default=...)
    sales_channel_domain: ForeignRelation["SalesChannelDomain"] = Field(default=...)
    currency: ForeignRelation["Currency"] = Field(default=...)


class ProductExportEndpoint(AdminEndpoint[ProductExport]):
    name = "product_export"
    path = "/product-export"
    model_class = ProductExport


from .currency import Currency  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .sales_channel_domain import SalesChannelDomain  # noqa: E402
