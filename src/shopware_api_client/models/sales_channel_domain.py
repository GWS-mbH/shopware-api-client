from typing import Annotated

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField, RefersTo


class SalesChannelDomainBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "sales_channel_domain"

    url: str
    sales_channel_id: Annotated[IdField, RefersTo("sales_channel")]
    language_id: Annotated[IdField, RefersTo("language")]
    currency_id: Annotated[IdField, RefersTo("currency")]
    snippet_set_id: IdField
    hreflang_use_only_locale: bool | None = None
