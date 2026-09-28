from typing import Annotated

from shopware_api_client.base import ApiModelBase
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class DocumentBaseConfigSalesChannelBase(ApiModelBase):
    _identifier: str = "document_base_config_sales_channel"

    document_base_config_id: Annotated[IdField, RefersTo("document_base_config")]
    sales_channel_id: Annotated[IdField | None, RefersTo("sales_channel")] = None
    document_type_id: Annotated[IdField | None, RefersTo("document_type")] = None
