from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class CountryStateBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "country_state"

    country_id: IdField
    short_code: str
    name: str
    position: int | None = None
    active: bool | None = None
