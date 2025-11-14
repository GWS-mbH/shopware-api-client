from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField


class DocumentBaseConfigSalesChannelBase(ApiModelBase):
    _identifier: str = "document_base_config_sales_channel"

    document_base_config_id: IdField
    sales_channel_id: IdField | None = None
    document_type_id: IdField | None = None
