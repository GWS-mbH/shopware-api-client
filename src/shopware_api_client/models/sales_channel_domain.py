from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class SalesChannelDomainBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "sales_channel_domain"

    url: str
    sales_channel_id: IdField
    language_id: IdField
    currency_id: IdField
    snippet_set_id: IdField
    hreflang_use_only_locale: bool | None = None
