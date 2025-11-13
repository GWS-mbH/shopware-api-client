from pydantic import Field

from shopware_api_client.base import ApiModelBase, CustomFieldsMixin
from shopware_api_client.endpoints.base_fields import IdField

_FILED_DESCRIPTION = "Runtime field, cannot be used as part of the criteria."


class PaymentMethodBase(ApiModelBase, CustomFieldsMixin):
    _identifier: str = "payment_method"

    plugin_id: IdField | None = None
    handler_identifier: str | None = None
    name: str
    distinguishable_name: str | None = Field(default=None, exclude=True)
    description: str | None = None
    position: int | None = None
    active: bool | None = None
    after_order_enabled: bool | None = None
    availability_rule_id: IdField | None = None
    media_id: IdField | None = None
    formatted_handler_identifier: str | None = Field(None, description=_FILED_DESCRIPTION, exclude=True)
    synchronous: bool | None = Field(None, description=_FILED_DESCRIPTION, exclude=True)
    asynchronous: bool | None = Field(None, description=_FILED_DESCRIPTION, exclude=True)
    prepared: bool | None = Field(None, description=_FILED_DESCRIPTION, exclude=True)
    refundable: bool | None = Field(None, description=_FILED_DESCRIPTION, exclude=True)
    recurring: bool | None = Field(None, description=_FILED_DESCRIPTION, exclude=True)
    short_name: str | None = Field(None, description=_FILED_DESCRIPTION)
    technical_name: str | None = Field(default=None, exclude=True)
