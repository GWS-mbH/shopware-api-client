from typing import Any, Annotated

from pydantic import Field, StringConstraints

from shopware_api_client.fieldsets import FieldSetBase

IdField = Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{32}$")]


class Data(FieldSetBase):
    states: list[dict[str, Any]] | None = Field(default=None)
    zip_code: str | None = None
    from_zip_code: str | None = None
    to_zip_code: str | None = None


class Visibility(FieldSetBase):
    mobile: bool | None = None
    desktop: bool | None = None
    tablet: bool | None = None
