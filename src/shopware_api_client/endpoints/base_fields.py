from typing import Annotated, Any

from pydantic import AliasChoices, AliasGenerator, BaseModel, ConfigDict, StringConstraints
from pydantic.alias_generators import to_camel

IdField = Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{32}$")]


class BaseFieldSet(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field_name: AliasChoices(field_name, to_camel(field_name)),
            serialization_alias=lambda field_name: to_camel(field_name),
        ),
        validate_assignment=True,
    )


class CustomerTax(BaseFieldSet):
    enabled: bool
    currency_id: IdField
    amount: float


class CompanyTax(BaseFieldSet):
    enabled: bool
    currency_id: IdField
    amount: float


class Data(BaseFieldSet):
    states: list[dict[str, Any]] | None = None
    zip_code: str | None = None
    from_zip_code: str | None = None
    to_zip_code: str | None = None


class Visibility(BaseFieldSet):
    mobile: bool | None = None
    desktop: bool | None = None
    tablet: bool | None = None


class ListPrice(BaseFieldSet):
    price: float | None = None
    discount: float | None = None
    percentage: float | None = None


class Price(BaseFieldSet):
    net_price: float
    total_price: float
    calculated_taxes: list[dict[str, Any]] | None = None
    tax_rules: list[dict[str, Any]] | None = None
    position_price: float
    raw_total: float
    tax_status: str


class RegulationPrice(BaseFieldSet):
    price: float | None = None


class Rounding(BaseFieldSet):
    decimals: int | None = None
    interval: float | None = None
    round_for_net: bool | None = None


class Amount(BaseFieldSet):
    unit_price: float
    total_price: float
    quantity: int
    calculated_taxes: list[dict[str, Any]] | None = None
    tax_rules: list[dict[str, Any]] | None = None
    reference_price: dict[str, Any] | None = None
    list_price: ListPrice | None = None
    regulation_price: RegulationPrice | None = None
