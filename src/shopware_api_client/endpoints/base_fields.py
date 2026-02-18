from typing import Annotated, Any

from pydantic import Field, StringConstraints, ValidationInfo, ValidatorFunctionWrapHandler, WrapValidator

from shopware_api_client.fieldsets import FieldSetBase


def normalize_php_assoc_array(
    value: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
) -> dict[str, Any] | None:
    if isinstance(value, dict):
        return value
    elif isinstance(value, list):
        if len(value) > 0:
            raise ValueError("Expected an associative array, but got a non-empty list")
        return {}
    elif value is None:
        return None
    else:
        raise ValueError(f"Expected an associative array, but got {type(value).__name__}")


IdField = Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{32}$")]
PhpAssocArray = Annotated[dict[str, Any] | None, WrapValidator(normalize_php_assoc_array)]


class Data(FieldSetBase):
    states: list[dict[str, Any]] | None = Field(default=None)
    zip_code: str | None = None
    from_zip_code: str | None = None
    to_zip_code: str | None = None


class Visibility(FieldSetBase):
    mobile: bool | None = None
    desktop: bool | None = None
    tablet: bool | None = None
