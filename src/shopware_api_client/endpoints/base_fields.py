from typing import Annotated, Any

from pydantic import AliasChoices, BaseModel, Field, StringConstraints

IdField = Annotated[str, StringConstraints(pattern=r"^[0-9a-f]{32}$")]


class CustomerTax(BaseModel):
    enabled: bool
    currency_id: str = Field(
        ..., serialization_alias="currencyId", validation_alias=AliasChoices("currency_id", "currencyId")
    )
    amount: float


class CompanyTax(BaseModel):
    enabled: bool
    currency_id: str = Field(
        ..., serialization_alias="currencyId", validation_alias=AliasChoices("currency_id", "currencyId")
    )
    amount: float


class Data(BaseModel):
    states: list[dict[str, Any]] | None = None
    zip_code: str | None = Field(
        default=None, serialization_alias="zipCode", validation_alias=AliasChoices("zip_code", "zipCode")
    )
    from_zip_code: str | None = Field(
        default=None, serialization_alias="fromZipCode", validation_alias=AliasChoices("from_zip_code", "fromZipCode")
    )
    to_zip_code: str | None = Field(
        default=None, serialization_alias="toZipCode", validation_alias=AliasChoices("to_zip_code", "toZipCode")
    )


class Visibility(BaseModel):
    mobile: bool | None = None
    desktop: bool | None = None
    tablet: bool | None = None


class ListPrice(BaseModel):
    price: float | None = None
    discount: float | None = None
    percentage: float | None = None


class Price(BaseModel):
    net_price: float = Field(
        ..., serialization_alias="netPrice", validation_alias=AliasChoices("net_price", "netPrice")
    )
    total_price: float = Field(
        ..., serialization_alias="totalPrice", validation_alias=AliasChoices("total_price", "totalPrice")
    )
    calculated_taxes: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="calculatedTaxes",
        validation_alias=AliasChoices("calculated_taxes", "calculatedTaxes"),
    )
    tax_rules: dict[str, Any] | None = Field(
        default=None, serialization_alias="taxRules", validation_alias=AliasChoices("tax_rules", "taxRules")
    )
    position_price: float = Field(
        ..., serialization_alias="positionPrice", validation_alias=AliasChoices("position_price", "positionPrice")
    )
    raw_total: float = Field(
        ..., serialization_alias="rawTotal", validation_alias=AliasChoices("raw_total", "rawTotal")
    )
    tax_status: str = Field(
        ..., serialization_alias="taxStatus", validation_alias=AliasChoices("tax_status", "taxStatus")
    )


class RegulationPrice(BaseModel):
    price: float | None = None


class Rounding(BaseModel):
    decimals: int | None = None
    interval: float | None = None
    round_for_net: bool | None = Field(
        default=None, serialization_alias="roundForNet", validation_alias=AliasChoices("round_for_net", "roundForNet")
    )


class Amount(BaseModel):
    unit_price: float = Field(
        ..., serialization_alias="unitPrice", validation_alias=AliasChoices("unit_price", "unitPrice")
    )
    total_price: float = Field(
        ..., serialization_alias="totalPrice", validation_alias=AliasChoices("total_price", "totalPrice")
    )
    quantity: int
    calculated_taxes: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="calculatedTaxes",
        validation_alias=AliasChoices("calculated_taxes", "calculatedTaxes"),
    )
    tax_rules: dict[str, Any] | None = Field(
        default=None, serialization_alias="taxRules", validation_alias=AliasChoices("tax_rules", "taxRules")
    )
    reference_price: dict[str, Any] | None = Field(
        default=None,
        serialization_alias="referencePrice",
        validation_alias=AliasChoices("reference_price", "referencePrice"),
    )
    list_price: ListPrice | None = Field(
        default=None, serialization_alias="listPrice", validation_alias=AliasChoices("list_price", "listPrice")
    )
    regulation_price: RegulationPrice | None = Field(
        default=None,
        serialization_alias="regulationPrice",
        validation_alias=AliasChoices("regulation_price", "regulationPrice"),
    )
