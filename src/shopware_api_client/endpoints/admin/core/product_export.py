from pydantic import AwareDatetime

from ....base import ApiModelBase, EndpointBase, EndpointClass
from ...base_fields import IdField
from ...relations import ForeignRelation


class ProductExportBase(ApiModelBase[EndpointClass]):
    _identifier: str = "product_export"

    product_stream_id: IdField
    storefront_sales_channel_id: IdField
    sales_channel_id: IdField
    sales_channel_domain_id: IdField
    currency_id: IdField
    file_name: str
    access_key: str
    encoding: str
    file_format: str
    include_variants: bool | None = None
    generate_by_cronjob: bool
    generated_at: AwareDatetime | None = None
    interval: int
    header_template: str | None = None
    body_template: str | None = None
    footer_template: str | None = None
    paused_schedule: bool | None = None
    is_running: bool | None = None


class ProductExportRelations:
    product_stream: ForeignRelation["ProductStream"]
    storefront_sales_channel: ForeignRelation["SalesChannel"]
    sales_channel: ForeignRelation["SalesChannel"]
    sales_channel_domain: ForeignRelation["SalesChannelDomain"]
    currency: ForeignRelation["Currency"]


class ProductExport(ProductExportBase["ProductExportEndpoint"], ProductExportRelations):
    pass


class ProductExportEndpoint(EndpointBase[ProductExport]):
    name = "product_export"
    path = "/product-export"
    model_class = ProductExport


from .currency import Currency  # noqa: E402
from .product_stream import ProductStream  # noqa: E402
from .sales_channel import SalesChannel  # noqa: E402
from .sales_channel_domain import SalesChannelDomain  # noqa: E402
