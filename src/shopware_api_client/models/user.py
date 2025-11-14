from pydantic import AwareDatetime

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField


class UserBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "user"

    locale_id: IdField
    username: str
    first_name: str
    last_name: str
    password: str | None = None
    title: str | None = None
    email: str
    active: bool | None = None
    admin: bool | None = None
    last_updated_password_at: AwareDatetime | None = None
    time_zone: str
    avatar_id: IdField | None = None
