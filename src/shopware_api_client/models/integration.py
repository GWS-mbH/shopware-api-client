from pydantic import AwareDatetime

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin


class IntegrationBase(ApiModelBase, CustomFieldsMixin):
    _identifier = "integration"

    label: str
    access_key: str
    secret_access_key: str
    last_usage_at: AwareDatetime | None = None
    admin: bool | None = None
    deleted_at: AwareDatetime | None = None
    write_access: bool | None = None
