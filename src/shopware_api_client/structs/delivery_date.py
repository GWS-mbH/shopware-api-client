from pydantic import AwareDatetime

from shopware_api_client.fieldsets import FieldSetBase


class DeliveryDate(FieldSetBase):
    earliest: AwareDatetime | None = None
    latest: AwareDatetime | None = None
