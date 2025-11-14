from typing import Any, Annotated

from pydantic import StringConstraints

from shopware_api_client.fieldsets import FieldSetBase

IdField = Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{32}$")]


class CustomerTax(FieldSetBase):
    enabled: bool
    currency_id: IdField
    amount: float


class CompanyTax(FieldSetBase):
    enabled: bool
    currency_id: IdField
    amount: float


class Data(FieldSetBase):
    states: list[dict[str, Any]] | None = None
    zip_code: str | None = None
    from_zip_code: str | None = None
    to_zip_code: str | None = None


class Visibility(FieldSetBase):
    mobile: bool | None = None
    desktop: bool | None = None
    tablet: bool | None = None


class ListPrice(FieldSetBase):
    price: float | None = None
    discount: float | None = None
    percentage: float | None = None


class Price(FieldSetBase):
    net_price: float
    total_price: float
    calculated_taxes: list[dict[str, Any]] | None = None
    tax_rules: list[dict[str, Any]] | None = None
    position_price: float
    raw_total: float
    tax_status: str


class RegulationPrice(FieldSetBase):
    price: float | None = None


class Rounding(FieldSetBase):
    decimals: int | None = None
    interval: float | None = None
    round_for_net: bool | None = None


class Amount(FieldSetBase):
    unit_price: float
    total_price: float
    quantity: int
    calculated_taxes: list[dict[str, Any]] | None = None
    tax_rules: list[dict[str, Any]] | None = None
    reference_price: dict[str, Any] | None = None
    list_price: ListPrice | None = None
    regulation_price: RegulationPrice | None = None
