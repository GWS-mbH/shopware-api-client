from shopware_api_client.base import ApiModelBase


class CustomField(ApiModelBase):
    _identifier: str = "custom_field"

    name: str
    custom_field_set_id: str | None = None
