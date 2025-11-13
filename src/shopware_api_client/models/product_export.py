from pydantic import AwareDatetime

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class ProductExportBase(ApiModelBase):
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
