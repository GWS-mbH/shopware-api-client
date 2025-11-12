from typing import Literal

from shopware_api_client.fieldsets import FieldSetBase


class MeasurementUnits(FieldSetBase):
    system: Literal["metric", "imperial"] | None = None
    units: dict[str, str] | None = None
