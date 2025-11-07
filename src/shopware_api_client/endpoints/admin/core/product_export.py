from shopware_api_client.base import AdminModel, AdminEndpoint
from shopware_api_client.endpoints.relations import ForeignRelation
from shopware_api_client.models.product_export import ProductExport as ProductExportBase


class ProductExport(ProductExportBase, AdminModel["ProductExportEndpoint"]):
    product_stream: ForeignRelation["ProductStream"]
    storefront_sales_channel: ForeignRelation["SalesChannel"]
    sales_channel: ForeignRelation["SalesChannel"]
    sales_channel_domain: ForeignRelation["SalesChannelDomain"]
    currency: ForeignRelation["Currency"]


class ProductExportEndpoint(AdminEndpoint[ProductExport]):
    name = "product_export"
    path = "/product-export"
    model_class = ProductExport


from .currency import Currency  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .sales_channel_domain import SalesChannelDomain  # noqa: E402
